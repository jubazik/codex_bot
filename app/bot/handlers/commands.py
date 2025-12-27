from telebot import types
from telebot.async_telebot import logger
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.menu import categories_keyboard, ReplyKeyboardMarkup, categories_bras, menu_
from app.sql.psql import database
from app.bot.config.settings import bot






@bot.callback_query_handler(func=lambda call: True)
async def callback_query(call):
    try:
        # Обработка выбора категории
        if call.data.startswith("category_"):
            category_id = int(call.data.split("_")[1])
            category = database.get_category_id(category_id)

            # if category:
            #     # Отправляем фото категории с описанием и кнопками товаров
            #     caption = f"*{category.name}*\n\n{category.description}\n\n👇 Выберите товар:"
            #
            #     # Если нужно отправить реальное фото
            #     await bot.send_photo(
            #         call.message.chat.id,
            #         category.photo_url,
            #         caption=caption,
            #         parse_mode="Markdown",
            #         reply_markup=products_keyboard(category_id)
            #     )
            #
            #     # Временно отправляем текстовое сообщение (замените на фото)
            #     # await bot.edit_message_text(
            #     #     chat_id=call.message.chat.id,
            #     #     message_id=call.message.message_id,
            #     #     text=caption,
            #     #     parse_mode="Markdown",
            #     #     reply_markup=products_keyboard(category_id)
            #     # )
            # else:
            #     await bot.answer_callback_query(call.id, "Категория не найдена")

        # Обработка кнопки "Назад"
        elif call.data == "back_to_categories":
            await bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="📂 Выберите категорию товаров:",
                parse_mode="Markdown",
                reply_markup=categories_keyboard()
            )

        # Обработка выбора товара
        # elif call.data.startswith("product_"):
        #     product_id = int(call.data.split("_")[1])
        #
        #     # Здесь можно получить информацию о товаре из БД
        #     product_info = f"Товар #{product_id}\nЦена: 1500₽\n\nДобавить в корзину?"
        #
        #     keyboard = InlineKeyboardMarkup()
        #     keyboard.add(
        #         InlineKeyboardButton("🛒 Добавить в корзину", callback_data=f"add_{product_id}"),
        #         InlineKeyboardButton("⬅️ Назад", callback_data="back_to_current_category")
        #     )
        #
        #     await bot.edit_message_text(
        #         chat_id=call.message.chat.id,
        #         message_id=call.message.message_id,
        #         text=product_info,
        #         reply_markup=keyboard
        #     )

        # Обработка корзины
        elif call.data == "bras":
            await bot.edit_message_text(chat_id=call.message.chat.id,  message_id=call.message.message_id, text="🎽 БЮСТГАЛЬТЕРЫ", reply_markup=categories_bras())

        # Обработка контактов
        elif call.sen_message == "ℹ️ О нас / Контакты":
            await bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="📞 Наши контакты:\n\nТелефон: +7 (XXX) XXX-XX-XX\nEmail: shop@example.com\nАдрес: г. Москва, ул. Примерная, д. 1",
                # reply_markup=InlineKeyboardMarkup().add(
                #     InlineKeyboardButton("⬅️ Назад", callback_data="back_to_categories")
                # )
            )

    except Exception as e:
        logger.error(f"Error in callback: {e}")
        await bot.answer_callback_query(call.id, "Произошла ошибка")


@bot.message_handler(func=lambda message: message.text=="ℹ️ О нас / Контакты")
async def about_contacts(message):
    await bot.send_message(message.chat.id,
        text="📞 Наши контакты:\n\n"
             "Телефон: +7 (XXX) XXX-XX-XX\n"
             "Email: shop@example.com\n"
             "Адрес: г. Москва, ул. Примерная, д. 1",
        reply_markup=menu_()
    )

@bot.message_handler(func=lambda message: message.text=="🛍️ Каталог")
async def catalog(message):
    await bot.send_message(message.chat.id, text='📋 Доступные категории:', reply_markup=categories_keyboard())


# Обработчик входящих фото
@bot.message_handler(content_types=['photo'])
async def handle_received_photo(message):
    # Получаем фото
    photo = message.photo[-1]

    # Благодарим пользователя
    await bot.reply_to(
        message,
        f"✅ Фото получено!\n"
        f"Размер: {photo.width}x{photo.height}\n"
        f"File ID: {photo.file_id[:20]}..."
    )

    # Можно отправить фото обратно
    await bot.send_photo(
        message.chat.id,
        photo.file_id,
        caption="Ваше фото 📷"
    )


@bot.message_handler(commands=['get'])
async def get_message(message):
    if database.get_user(message.from_user.id)  == message.from_user.id:
        await bot.send_message(message.chat.id, database.get_user(message.from_user.id))



@bot.message_handler(commands=['users'])
async def get_users(message):
    users_ = database.get_user(message.from_user.id)
    await bot.send_message(message.chat.id, users_ )

@bot.message_handler(commands=['delete'])
async def delete_message(message):
    try:
        if database.get_user(message.from_user.id):
            database.delete_user(message.from_user.id)
            await bot.send_message(message.chat.id, f'пользователь {message.from_user.first_name} успешно удален ')

        else:
            await bot.send_message(message.chat.id, 'Пользоваетеля нет в базе')
    except:
        await bot.send_message(message.chat.id,'произошла ошибка')
