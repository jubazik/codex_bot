from telebot.types import  MenuButtonWebApp, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

def menu_():
    markup = ReplyKeyboardMarkup(
        resize_keyboard=False,
        one_time_keyboard=True,
        selective=True,
    )

    markup.row(
        KeyboardButton("кнопка_1", request_contact=False),
        KeyboardButton('Кнопка_2', request_contact=False)
    )

    markup.row(
        KeyboardButton("кнопка_3", request_contact=True),
        KeyboardButton('Кнопка_4', request_contact=False),

    )
    markup.row("Меню", "Помощь", "Настройки")
    return markup




