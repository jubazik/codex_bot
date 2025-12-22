from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv

import os

load_dotenv()
token = os.getenv('TELEGRAM_BOT_TOKEN')
if not token:
    raise Exception("Токен не найден в переменных окружения")



bot = AsyncTeleBot(token=token)
