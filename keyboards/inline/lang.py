from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

laguage =InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="🇬🇧 English", callback_data="en"),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru")
    ],
    [
        InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz"),

    ]
]
)

laguageuz =InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="🇬🇧 English", callback_data="en"),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru"),

    ],
    [
        InlineKeyboardButton(text="🇺🇿 O'zbekcha ✅", callback_data="uz"),
    ]
]
)

laguageen =InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="🇬🇧 English ✅", callback_data="en"),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru")
    ],
    [
        InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz"),
    ]
]
)

laguageru =InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="🇬🇧 English", callback_data="en"),
        InlineKeyboardButton(text="🇷🇺 Русский ✅", callback_data="ru")
    ],
    [
        InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz"),
    ]
]
)
