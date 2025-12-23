
from telebot.async_telebot import AsyncTeleBot
import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = AsyncTeleBot(BOT_TOKEN)

# Инициализация бота (без импорта хендлеров здесь)
def init_bot():
    """Функция для инициализации бота"""
    return bot