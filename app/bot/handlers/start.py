from telebot.types import  MenuButtonWebApp, WebAppInfo
from app.bot.config.settings import bot
from app.sql.psql import users
from menu import menu_


def get_menu():
    from menu import menu_
    return menu_

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    try:
        if users.get_user(message.from_user.id) is  None:
            users.new_user(message.from_user.id, message.from_user.first_name, message.from_user.last_name)
            await bot.send_message(message.from_user.id,
                                   f'Добро пожаловать {message.from_user.first_name} Vbbetli VPN  предоставляет вам интернет без ограничений лимитный трафик')
        else:
            commands = MenuButtonWebApp(
                type="web_app",
                text = 'VPN',
                web_app = WebAppInfo(url="https://vpbetli.ru:23421/panel/")
            )

            await bot.set_chat_menu_button(chat_id=message.from_user.id, menu_button=commands)
            await bot.send_message(message.chat.id,
                                   text=f'Добро пожаловать {message.from_user.first_name} Какие будут указании! {users.get_user(message.from_user.id)}', reply_markup=menu_())


    except Exception as e:  # перехватываем все исключения

        await bot.send_message(message.chat.id, f"Произошла ошибка {str(e)} обратитесь к администратору!")

        print(f"Произошла ошибка {str(e)} обратитесь к администратору!")