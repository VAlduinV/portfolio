[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
[![Static Badge](https://img.shields.io/badge/fastapi-violet)](https://fastapi.tiangolo.com/)
[![Static Badge](https://img.shields.io/badge/Redis-red)](https://redis.io/docs/)

# Hacker news

**This code is a FastAPI application that interacts with the Hacker News API to retrieve and cache information about news and comments. The main features of the app include:**

* Connecting to Redis: The aioredis library is used to connect to the Redis server.

* **fetch_story(story_id, redis):** Function for obtaining information about the news 
(by its identifier story_id). If the news is already stored in Redis, it is pulled from the cache. 
If not, a request is made to the Hacker News API and the news is stored in Redis for later use.

* **fetch_comment(comment_id, redis):** Function to get information about a comment (by its identifier 
comment_id). If the comment is already stored in Redis, it is pulled from the cache. If not, a request is made to the Hacker News API and the comment is stored in Redis with a time limit for caching.

* **fetch_comments(story, redis):** Function for getting comments on a certain news. It first checks for 
comments in the cache and retrieves them if they are there. It then queries the Hacker News API for comments that are not in the cache and caches them in Redis.

* **/topstories/:** Application root path for top ten news list. Querying the Hacker News API for a list of 
news items limited to the first ten, information is extracted from each news item, including the ID, title, text, and publication time.

* **/stories/{story_id}:** Path to get information about a specific news by its story_id identifier. 
News information is retrieved from Redis, and if a news story is found, its comments are retrieved, 
including their text and other data.

**The app also runs using the uvicorn library at address "0.0.0.0" and port 8000 to provide an API for receiving news and comments from the Hacker News API.**

**This application demonstrates the use of asynchronous programming and caching to improve performance when interacting with external APIs.**