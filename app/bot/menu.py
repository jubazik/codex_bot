from telebot.types import MenuButtonWebApp, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
from app.sql.psql import database

def menu_():
    markup = ReplyKeyboardMarkup(
        resize_keyboard=False,
        one_time_keyboard=True,
        selective=True,
    )

    markup.row(
        KeyboardButton("Футболки", request_contact=False),
        KeyboardButton('Джинсы', request_contact=False)
    )

    markup.row(
        KeyboardButton("Обувь", request_contact=True),
        KeyboardButton('Куртки', request_contact=False),

    )
    markup.row("Корзина", "Помощь", "Контакты")
    return markup



def categories_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)

    buttons = [
        InlineKeyboardButton(text="👕 Футболки", callback_data="category_1"),
        InlineKeyboardButton(text="👖 Джинсы", callback_data="category_2"),
        InlineKeyboardButton(text="👟 Обувь", callback_data="category_3"),
        InlineKeyboardButton(text="🧥 Куртки", callback_data="category_4"),
        InlineKeyboardButton(text="🛒 Корзина", callback_data="cart"),
        InlineKeyboardButton(text="📞 Контакты", callback_data="contacts")
    ]

    # Добавляем кнопки по две в ряд
    for i in range(0, len(buttons), 2):
        if i + 1 < len(buttons):
            keyboard.add(buttons[i], buttons[i + 1])
        else:
            keyboard.add(buttons[i])

    return keyboard


# Клавиатура для товаров в категории
def products_keyboard(category_id: int):
    category = database.get_category_id(category_id)
    if not category:
        return None

    keyboard = InlineKeyboardMarkup()

    # Кнопки для каждого товара в категории
    for product in category.products:
        keyboard.add(InlineKeyboardButton(
            text=f"{product['name']} - {product['price']}₽",
            callback_data=f"product_{product['id']}"
        ))

    # Кнопка "Назад к категориям"
    keyboard.add(InlineKeyboardButton(
        text="⬅️ Назад к категориям",
        callback_data="back_to_categories"
    ))

    return keyboard

