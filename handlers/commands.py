from sql.psql import users
from config.settings import bot


# @bot.message_handler(commands=['get'])
# async def get_message(message):
#     if users.get_user(message.from_user.id)  == message.from_user.id:
#         await bot.send_message(message.chat.id
# #
# @bot.message_handler(commands=['users'])
# async def get_users(message):
#     users_ = users.get_user(message.from_user.id)
#     await bot.send_message(message.chat.id, users_ )

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
