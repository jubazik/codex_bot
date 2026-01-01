from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton


def menu_():
    markup = ReplyKeyboardMarkup(
        resize_keyboard=False,
        one_time_keyboard=True,
        selective=True,
    )

    markup.row(
        KeyboardButton("🛍️ Каталог ", request_contact=False),
        KeyboardButton('🔍 Поиск ', request_contact=False)
    )

    markup.row(
        KeyboardButton("⭐ Избранное", request_contact=False),
    )
    markup.row(
        KeyboardButton("📦 Мои заказы", request_contact=False, ),
        KeyboardButton('🛒 Корзина ', request_contact=False),

    )
    markup.row("📞 Поддержка / Помощь ", "⚙️ Настройки / Профиль", "ℹ️ О нас / Контакты")
    return markup

def categories_bras():

    """
    Меню категории бюстгалтеры

    """
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text="Без косточек", callback_data="Seedless"),
        InlineKeyboardButton(text="С косточками", callback_data="with_bones"),
        InlineKeyboardButton(text="Пуш-ап", callback_data="push_up"),
        InlineKeyboardButton(text="Балконет", callback_data="balconette"),
        InlineKeyboardButton(text="Спортивные", callback_data="sports"),
        InlineKeyboardButton(text="Балконет", callback_data="balconette"),
        InlineKeyboardButton(text="Для кормления", callback_data="for_feeding"),
        InlineKeyboardButton(text="Повседневные", callback_data="everyday"),
        InlineKeyboardButton(text="Вечерние", callback_data="evening"),
        InlineKeyboardButton(text="Кружевные", callback_data="lace"),
        InlineKeyboardButton(text="Хлопковые ", callback_data="cotton"),
        InlineKeyboardButton(text="🎯 Подобрать по размеру ", callback_data="select_by_size"),
        InlineKeyboardButton(text="❓ Как выбрать? ", callback_data="how_to_choose"),
        InlineKeyboardButton(text="🔙 Назад ", callback_data="back_to_categories"),
    ]
    for i in range(0, len(buttons), 2):
        if i + 1 < len(buttons):
            keyboard.add(buttons[i], buttons[i + 1])
        else:
            keyboard.add(buttons[i])

    return keyboard
def categories_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)

    buttons = [
        InlineKeyboardButton(text="Бюстгальтеры", callback_data="bras"),
        InlineKeyboardButton(text="Комплекты", callback_data="kits"),
        InlineKeyboardButton(text=" 🏃‍♀️  Спортивное ", callback_data="sports"),
        InlineKeyboardButton(text="✨ Свадебное ", callback_data="wedding"),
        InlineKeyboardButton(text="💤 Для сна  ", callback_data="For_sleep"),
        InlineKeyboardButton(text="Трусики ", callback_data="panties"),
        InlineKeyboardButton(text="🤰 Для беременных ", callback_data="For_pregnant_women"),
        InlineKeyboardButton(text="🩲 Корректирующее ", callback_data="corrective"),
        InlineKeyboardButton(text="🎯 ПОМОЩЬ В ВЫБОРЕ  ", callback_data="help_in_choosing"),
        InlineKeyboardButton(text="💰 РАСПРОДАЖА   ", callback_data="sale"),
        InlineKeyboardButton(text="🔍 Поиск   ", callback_data="search"),
        InlineKeyboardButton(text="🆕 НОВИНКИ  ", callback_data="new"),
    ]

    # Добавляем кнопки по две в ряд
    for i in range(0, len(buttons), 2):
        if i + 1 < len(buttons):
            keyboard.add(buttons[i], buttons[i + 1])
        else:
            keyboard.add(buttons[i])

    return keyboard

#
# # Клавиатура для товаров в категории
# def products_keyboard(category_id: int):
#     category = database.get_category_id(category_id)
#     if not category:
#         return None
#
#     keyboard = InlineKeyboardMarkup()
#
#     # Кнопки для каждого товара в категории
#     for product in category.products:
#         keyboard.add(InlineKeyboardButton(
#             text=f"{product['name']} - {product['price']}₽",
#             callback_data=f"product_{product['id']}"
#         ))
#
#     # Кнопка "Назад к категориям"
#     keyboard.add(InlineKeyboardButton(
#         text="⬅️ Назад к категориям",
#         callback_data="back_to_categories"
#     ))
#
#     return keyboard

