from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


from loader import dp, db, bot
zakazid = 1
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
            InlineKeyboardButton(text=f"Page 1/1",callback_data='page'),
            InlineKeyboardButton(text="▶️",callback_data='keyin')
        ]
    ]
)
