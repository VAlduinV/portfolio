from fastapi import FastAPI, HTTPException, Depends
import httpx
import json
import asyncio
from httpx import ReadTimeout
import aioredis

# Constants
HACKERNEWS_API = "https://hacker-news.firebaseio.com/v0"

app = FastAPI()


# connect async redis
async def get_redis():
    redis = await aioredis.Redis.from_url("redis://localhost:6379/0")
    try:
        yield redis
    finally:
        await redis.close()


async def fetch_story(story_id: int, redis: aioredis.Redis):
    cache_key = f"hn:story:{story_id}"
    cached_story = await redis.get(cache_key)
    if cached_story:
        return json.loads(cached_story.decode('utf-8'))

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{HACKERNEWS_API}/item/{story_id}.json")
        if response.status_code == 200:
            story = response.json()
            await redis.set(cache_key, json.dumps(story))
            return story
    return None


async def fetch_comment(comment_id, redis):
    cached_comment = await redis.get(f"comment:{comment_id}")
    if cached_comment:
        print(f"Comment {comment_id} retrieved from Redis cache!")
        return json.loads(cached_comment)

    # logs
    print(f"Comment {comment_id} not in cache, fetching from API...")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{HACKERNEWS_API}/item/{comment_id}.json")
        if response.status_code == 200:
            comment = response.json()
            await redis.setex(f"comment:{comment_id}", 60, json.dumps(comment))
            return comment


"""
Batch Caching: 
When retrieving multiple comments from Redis, mget is used. This is good, 
but after some comments have been retrieved from the API, they are cached individually. 
We can optimize this by using mset to cache missing comments in batches.
"""


async def fetch_comments(story, redis):
    comment_ids = story.get("kids", [])

    cache_keys = [f"comment:{comment_id}" for comment_id in comment_ids]
    cached_comments = await redis.mget(cache_keys)

    comments = []
    missing_comment_ids = []
    missing_comments = []

    for idx, cached_comment in enumerate(cached_comments):
        if cached_comment:
            comments.append(json.loads(cached_comment.decode('utf-8')))
        else:
            missing_comment_ids.append(comment_ids[idx])

    if missing_comment_ids:  # Only do API calls if there are missing comments
        missing_comments = await asyncio.gather(
            *[fetch_comment(comment_id, redis) for comment_id in missing_comment_ids])
        comments.extend([comment for comment in missing_comments if comment])

        # Optimize caching of the missing comments using mset
        comment_dict = {}
        for comment_id, comment in zip(missing_comment_ids, missing_comments):
            comment_dict[f"comment:{comment_id}"] = json.dumps(comment)
        await redis.mset(comment_dict)

    return comments


@app.get("/topstories/")
async def get_top_stories(redis: aioredis.Redis = Depends(get_redis)):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{HACKERNEWS_API}/topstories.json")
        if response.status_code == 200:
            top_stories_ids = response.json()[:10]
            top_stories = []
            for story_id in top_stories_ids:
                story = await fetch_story(story_id, redis)
                if story:
                    top_stories.append({
                        "id": story["id"],
                        "title": story.get("title", ""),
                        "text": story.get("text", ""),
                        "time": story["time"],
                    })
            return top_stories
    raise HTTPException(status_code=404, detail="Error fetching top stories")


@app.get("/stories/{story_id}")
async def get_story(story_id: int, redis: aioredis.Redis = Depends(get_redis)):
    story = await fetch_story(story_id, redis)
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")

    comments = await fetch_comments(story, redis)

    return {
        "id": story["id"],
        "text": story.get("text", ""),
        "comments": comments,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
