import json
from telethon.sync import TelegramClient
import configparser
from gender_guesser.detector import Detector

# Чтение данных из файла config.ini
config = configparser.ConfigParser()
config.read('C:\\Users\\prime\\PycharmProjects\\portfolio\\tgbot\\config\\config.ini')

api_id = config.getint('API', 'api_id')
api_hash = config.get('API', 'api_hash')
session_name = config.get('API', 'session_name')


async def fetch_group_members():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        group_entity = await client.get_entity(
            "")  # Посилання групи
        participants = await client.get_participants(group_entity)

        members_info = {}
        for user in participants:
            username = user.username
            if username:
                members_info[username] = {
                    "name": user.first_name,
                    "last_name": user.last_name,
                }

        return members_info


async def filter_and_save_members():
    members_info = await fetch_group_members()
    male_users = []
    female_users = []

    detector = Detector()

    for username, info in members_info.items():
        name = info.get("name")

        # Используем библиотеку gender_guesser для определения пола на основе имени
        gender = detector.get_gender(name)

        if gender in ['male', 'mostly_male']:
            male_users.append(username)
        elif gender in ['female', 'mostly_female']:
            female_users.append(username)

    # Запись имен в соответствующие файлы
    with open('gender/male.txt', 'w', encoding='utf-8') as male_file:
        male_file.write('\n'.join(male_users))

    with open('gender/female.txt', 'w', encoding='utf-8') as female_file:
        female_file.write('\n'.join(female_users))

    # Запись информации о пользователях в JSON файл
    with open('info/group_members.json', 'w', encoding='utf-8') as json_file:
        json.dump(members_info, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(filter_and_save_members())
