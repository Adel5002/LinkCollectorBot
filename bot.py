import os

from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')



bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))