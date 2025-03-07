import asyncio
import re
import csv
import os
from lib2to3.pgen2.literals import escape

from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram import Router
from telethon import TelegramClient

from dotenv import load_dotenv

load_dotenv()


router = Router()

client = TelegramClient('session_name', int(os.getenv('APP_API')), os.getenv('APP_HASH'))

async def test(entity, topic_id):
    await client.start(os.getenv('PHONE_NUM'))

    messages = await client.get_messages(entity, limit=1000, reply_to=topic_id)
    text = []
    for msg in messages:
        if msg.text is not None and msg.text.startswith('https://'):
            text.append(msg.text)

    return text

@router.message(Command('link_collector'))
async def get_links(message: Message):
    get_links_from_chats = await test(int(message.chat.id), message.message_thread_id)

    # Читаем ссылки из CSV и собираем их в set
    try:
        with open('csv_files/history/registry.csv', 'r', newline='', encoding='utf-8') as csvfile_open:
            file = csv.reader(csvfile_open)
            get_links_from_history = set(link for row in file for link in row)
            print(get_links_from_history)
    except FileNotFoundError:
        get_links_from_history = set()  # Если файла нет, создаем пустой set

    # Проверяем дубликаты
    new_links = []
    for link in get_links_from_chats:
        if re.search(r'item/(\d+)', link).group(1) not in get_links_from_history:
            new_links.append({'BuyID': re.search(r'item/(\d+)', link).group(1)})

    print(new_links)
    # Добавляем только новые ссылки
    if new_links:
        with open('csv_files/history/registry.csv', 'a', newline='', encoding='utf-8') as csvfile1, \
                open('csv_files/ready_links/links_for_ds.csv', 'w', newline='', encoding='utf-8') as csvfile2:
            fieldnames = ['BuyID']
            file1 = csv.DictWriter(csvfile1, fieldnames=fieldnames)
            file2 = csv.DictWriter(csvfile2, fieldnames=fieldnames)
            file1.writeheader()
            file2.writeheader()
            file1.writerows(new_links)
            file2.writerows(new_links)
        await message.answer("Ссылки добавлены!")
        await message.answer_document(FSInputFile(path='csv_files/ready_links/links_for_ds.csv'))
    else:
        await message.answer("Все ссылки уже есть в истории.")
