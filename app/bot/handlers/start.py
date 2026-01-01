from app.bot.config.settings import bot
from app.core.psql import database
from app.bot.menu import menu_


def get_menu():
    from app.bot.menu import menu_
    return menu_


@bot.message_handler(commands=['start'])
async def send_welcome(message):
    welcome_text = """
    👋 Добро пожаловать в наш магазин одежды!

    Здесь вы найдете:
    • Модную одежду
    • Качественные материалы
    • Доступные цены

    👇 Выберите категорию товаров:
        """
    try:
        if database.get_user(message.from_user.id) is None:
            database.new_user(message.from_user.id, message.from_user.first_name, message.from_user.last_name)
            await bot.send_message(message.chat.id, welcome_text, reply_markup=menu_())
            # await bot.send_message(message.chat.id, text='📋 Доступные категории:', reply_markup=categories_keyboard())

        else:
        #     commands = MenuButtonWebApp(
        #         type="web_app",
        #         text='Магазин',
        #         web_app=WebAppInfo(url="Нужно добавить url-адрес своего магазина")
        #     )

            # await bot.set_chat_menu_button(chat_id=message.from_user.id, menu_button=commands)
            await bot.send_message(message.chat.id, welcome_text, reply_markup=menu_())
            # await bot.send_message(message.chat.id, text='📋 Доступные категории:', reply_markup=categories_keyboard())


    except Exception as e:  # перехватываем все исключения

        await bot.send_message(message.chat.id, f"Произошла ошибка {str(e)} обратитесь к администратору!")

        print(f"Произошла ошибка {str(e)} обратитесь к администратору!")
