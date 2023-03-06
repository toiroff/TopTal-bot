from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default.kategoriya import soxa
from loader import dp,db
from states.kategoriya import kategoriya

menuuz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💼 Iste'dodlar"),
            KeyboardButton(text="  ℹ️ Nega TopTal")
        ],
        [
            KeyboardButton(text="📊 Darajalar"),
            # KeyboardButton(text="📃 Qo'llanma ")
        ],
        [
            KeyboardButton(text="🧑🏻‍💻 I'm Freelancer"),
            KeyboardButton(text="👥 I'm Client")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="🧑🏻‍💻 I'm Freelancer")
async def bot_start(message: types.Message):
    await message.answer(f"<b>🧑🏻‍💻 Men Frilanserman</b>" , reply_markup=frilans)
@dp.message_handler(text="👥 I'm Client")
async def bot_start(message: types.Message):
    await message.answer(f"<b>👤 Men buyurtmachiman</b>" , reply_markup=buyurtma)
@dp.message_handler(text="🔝 Asosiy Menyu")
async def bot_start(message: types.Message):
    await message.answer(f"🔝 <b>Asosiy Menyu</b>" , reply_markup=menuuz)


frilans = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔎 Search'),
        ],
        [
            KeyboardButton(text="📝 Mening  buyurtmalarim"),
            KeyboardButton(text='📬 Mening takliflarim'),
        ],

        [
            KeyboardButton(text="👤 Mening profilim"),
            KeyboardButton(text='📥 Buyurtma olish'),
        ],
        [KeyboardButton(text='🔝 Asosiy Menyu')]
    ],
    resize_keyboard=True
)


@dp.message_handler(text="🔙Back")
async def bot_start(message: types.Message):
    await message.answer(f"<b>🧑🏻‍💻 Men Frilanserman</b>" , reply_markup=frilans)

# Buyurtmachi ----------------------------------------------------------------------------
buyurtma=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💸 Frilanser bilan ishlar!")
        ],
        [
            KeyboardButton(text='🗂 Mening buyurtmalarim'),
            KeyboardButton(text='👨🏻‍💻 Freelancer takliflar'),
        ],
        [
            KeyboardButton(text="👤  Mening profilim"),
            KeyboardButton(text='📤 Buyurtma yaratish'),

        ],
        [
            KeyboardButton(text='🔝 Asosiy Menyu')
        ]

    ],
    resize_keyboard=True
)
sozlamarb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="®Men haqimda️")
        ],
        [
            KeyboardButton(text="🔙Back"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],resize_keyboard=True
)

Buyurtma = ReplyKeyboardMarkup(
    keyboard=[
        # [KeyboardButton(text="Orqaga")],
        [KeyboardButton(text="IT va dasturlash"),KeyboardButton(text='Dizayn')],
        [KeyboardButton(text='SEO va trafik'),KeyboardButton(text='Ijtimoiy tarmoq va reklama')],
        [KeyboardButton(text='Tekstlar va tarjimalar'),KeyboardButton(text='Audio, Video, tasvirga olish')]
    ],
    resize_keyboard=True
)
# Buyurtma END ----------------------------------------------------------------------------------------


@dp.message_handler(text="Kategoriyalar ☑️")
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=soxa)
    await kategoriya.ismi.set()

@dp.message_handler(state=kategoriya.ismi)
async def bot_start(message: types.Message, state:FSMContext):
    ism=message.text
    await state.update_data({'ism':ism})
    malumot=await state.get_data()
    ism=malumot.get('ism')
    baza=db.update_kategoriya(id=message.from_user.id,kategoriya=ism)
    await message.answer('Muvaffaqqiyatli amalga oshirildi ✅',reply_markup=frilans)
    await state.finish()






royxat = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Ro'yxatdan o'tish ➕", request_contact=True)]

    ],
    resize_keyboard=True
)

tasdiq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Tasdiqlash"),
            KeyboardButton(text="❌ Bekor qilish")
        ]
    ],
    resize_keyboard=True
)

tasdiqtaklif = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Xa"),
            KeyboardButton(text="❌ Yo'q")
        ]
    ],
    resize_keyboard=True
)


client_orqaga = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Orqaga")
        ]
    ],resize_keyboard=True
)
frilanser_orqaga = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ orqaga")
        ]
    ],resize_keyboard=True
)

inline_tugma = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="✅ Tasdiqlash", callback_data='takliftasdiq'),
                      InlineKeyboardButton(text="❌ Bekor qilish", callback_data='taklifbekor')],
                     ])

zakazdaraja = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Entry"),
            KeyboardButton(text="Middle"),
            KeyboardButton(text="Expert")
        ]
    ],resize_keyboard=True

)