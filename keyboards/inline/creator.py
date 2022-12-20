from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from loader import dp, db, bot

creator = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="© 2022 TopTal® Global Inc.",url="https://t.me/unityagency")
        ]
    ]
)

olish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀",callback_data='orqa'),
            InlineKeyboardButton(text="Page 1/10 ",callback_data='page'),
            InlineKeyboardButton(text="▶️",callback_data='keyin')
        ]
    ]
)
# olish2 = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="◀",callback_data='orqa2'),
#             InlineKeyboardButton(text="Page 2/10 ",callback_data='page2'),
#             InlineKeyboardButton(text="▶️",callback_data='keyin2')
#         ]
#     ]
# )
#
#
# @dp.message_handler(text="keyin")
# async def bot_start(message: CallbackQuery):
#     users = db.select_random_zakaz()
#     print(users, "buyurtmalar")
#     for user in users:
#         user_id = user[1]
#         ms_id = user[0]
#         inline_tugma = InlineKeyboardMarkup(
#             inline_keyboard=[[InlineKeyboardButton(text="Taklif kiritish", callback_data=f'taklif{ms_id}')]])
#         await  bot.send_message(message.from_user,text=f"{user_id}", reply_markup=inline_tugma)
#
#     await bot.send_message(message.from_user,text="....", reply_markup=olish2)