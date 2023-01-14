from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

soxa=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='IT va dasturlash'),
            KeyboardButton(text='Dizayin')
        ],
        [
            KeyboardButton(text='Seo va traffik'),
            KeyboardButton(text='Ijtimoiy tarmoq va reklama')
        ],
        [
            KeyboardButton(text='Tekslar va tarjimalar'),
            KeyboardButton(text='Audio, Video, Tasvirga olish')
        ]



    ],
    resize_keyboard=True
)