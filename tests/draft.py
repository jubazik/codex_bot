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



# @bot.message_handler(commands=['get'])
# async def get_message(message):
#     if database.get_user(message.from_user.id)  == message.from_user.id:
#         await bot.send_message(message.chat.id, database.get_user(message.from_user.id))
#
#
#
# @bot.message_handler(commands=['users'])
# async def get_users(message):
#     users_ = database.get_user(message.from_user.id)
#     await bot.send_message(message.chat.id, users_ )
#
# @bot.message_handler(commands=['delete'])
# async def delete_message(message):
#     try:
#         if database.get_user(message.from_user.id):
#             database.delete_user(message.from_user.id)
#             await bot.send_message(message.chat.id, f'пользователь {message.from_user.first_name} успешно удален ')
#
#         else:
#             await bot.send_message(message.chat.id, 'Пользоваетеля нет в базе')
#     except:
#         await bot.send_message(message.chat.id,'произошла ошибка')
