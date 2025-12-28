from telebot.async_telebot import logger
from app.bot.menu import categories_keyboard, categories_bras, menu_
from app.sql.psql import database
from app.bot.config.settings import bot
from app.text import help_text


@bot.callback_query_handler(func=lambda call: call.data == 'back_to_categories')
async def handle_back(call):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text='Выберите категорию товаров',
        parse_mode="Markdown",
        reply_markup=categories_keyboard()

    )


@bot.callback_query_handler(func=lambda call: call.data == 'bras')
async def handle_bras(call):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text="🎽 БЮСТГАЛЬТЕРЫ", reply_markup=categories_bras())



@bot.message_handler(func=lambda message: message.text == '📞 Поддержка / Помощь')
async def help(message):

    await bot.send_message(message.chat.id, text=help_text, reply_markup=menu_())


@bot.message_handler(func=lambda message: message.text == "ℹ️ О нас / Контакты")
async def about_contacts(message):
    await bot.send_message(message.chat.id,
                           text="📞 Наши контакты:\n\n"
                                "Телефон: +7 (XXX) XXX-XX-XX\n"
                                "Email: shop@example.com\n"
                                "Адрес: г. Москва, ул. Примерная, д. 1",
                           reply_markup=menu_()
                           )


@bot.message_handler(func=lambda message: message.text == "🛍️ Каталог")
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
