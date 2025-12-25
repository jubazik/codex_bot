from sql.psql import users
from config.settings import bot


@bot.message_handler(commands=['sendphoto'])
async def request_photo(message):
    await bot.reply_to(
        message,
        "📸 Пожалуйста, отправьте фото из вашей галереи или сделайте новое фото"
    )


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
    if users.get_user(message.from_user.id)  == message.from_user.id:
        await bot.send_message(message.chat.id, users.get_user(message.from_user.id))



@bot.message_handler(commands=['users'])
async def get_users(message):
    users_ = users.get_user(message.from_user.id)
    await bot.send_message(message.chat.id, users_ )

@bot.message_handler(commands=['delete'])
async def delete_message(message):
    try:
        if users.get_user(message.from_user.id):
            users.delete_user(message.from_user.id)
            await bot.send_message(message.chat.id, f'пользователь {message.from_user.first_name} успешно удален ')

        else:
            await bot.send_message(message.chat.id, 'Пользоваетеля нет в базе')
    except:
        await bot.send_message(message.chat.id,'произошла ошибка')
