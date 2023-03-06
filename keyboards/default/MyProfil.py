from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

profilbuyurtmachi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mening ma'lumotlarim 💾"),
            KeyboardButton(text="Ismni o'zgartirish ⬆️")

        ],
        [
            KeyboardButton(text="Raqamni o'zgartirish 📞"),
            KeyboardButton(text="🔙 Back")
        ]
    ],resize_keyboard=True
)
royxat1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Update Number ⬆️", request_contact=True)]

    ],
    resize_keyboard=True
)
profilfrilanser = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💾 Mening ma'lumotlarim"),
            KeyboardButton(text="Ismni o'zgartirish ⬆️")

        ],
        [
            KeyboardButton(text="Raqamni o'zgartirish 📞"),
            KeyboardButton(text="Kategoriyalar ☑️"),

        ],
        [
            KeyboardButton(text="Orqaga 🔙")
        ]
    ],resize_keyboard=True
)


