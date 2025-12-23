import asyncio
import sys
import os

# Добавляем текущую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Импортируем ВСЕ хендлеры ДО инициализации бота
import handlers.start  # Это зарегистрирует хендлер /start
import handlers.commands  # Если есть другие команды

from config.settings import bot


async def main():
    """Основная функция запуска бота"""
    print("Запуск бота...")

    # Дополнительная инициализация если нужно
    # handlers.register_handlers()

    # Запускаем бота
    await bot.polling()


if __name__ == "__main__":
    asyncio.run(main())