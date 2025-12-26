from telebot.async_telebot import AsyncTeleBot
import os
from dotenv import load_dotenv

from app.bot.config.config import settings

load_dotenv("/Users/juba/projects/codex/.env")

BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN

# Если token None, покажем все переменные окружения
if BOT_TOKEN is None:
    print("DEBUG: Все переменные окружения:")
    for key, value in os.environ.items():
        if 'TELEGRAM' in key.upper() or 'BOT' in key.upper():
            print(f"  {key} = {value}")
bot = AsyncTeleBot(settings.TELEGRAM_BOT_TOKEN)

# Инициализация бота (без импорта хендлеров здесь)
def init_bot():
    """Функция для инициализации бота"""
    return bot