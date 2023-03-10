from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default.kategoriya import soxa
from loader import dp,db
from states.kategoriya import kategoriya

menuuz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ð¼ Iste'dodlar"),
            KeyboardButton(text="  â¹ï¸ Nega TopTal")
        ],
        [
            KeyboardButton(text="ð Darajalar"),
            # KeyboardButton(text="ð Qo'llanma ")
        ],
        [
            KeyboardButton(text="ð§ð»âð» I'm Freelancer"),
            KeyboardButton(text="ð¥ I'm Client")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="ð§ð»âð» I'm Freelancer")
async def bot_start(message: types.Message):
    await message.answer(f"<b>ð§ð»âð» Men Frilanserman</b>" , reply_markup=frilans)
@dp.message_handler(text="ð¥ I'm Client")
async def bot_start(message: types.Message):
    await message.answer(f"<b>ð¤ Men buyurtmachiman</b>" , reply_markup=buyurtma)
@dp.message_handler(text="ð Asosiy Menyu")
async def bot_start(message: types.Message):
    await message.answer(f"ð <b>Asosiy Menyu</b>" , reply_markup=menuuz)


frilans = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ð Search'),
        ],
        [
            KeyboardButton(text="ð Mening  buyurtmalarim"),
            KeyboardButton(text='ð¬ Mening takliflarim'),
        ],

        [
            KeyboardButton(text="ð¤ Mening profilim"),
            KeyboardButton(text='ð¥ Buyurtma olish'),
        ],
        [KeyboardButton(text='ð Asosiy Menyu')]
    ],
    resize_keyboard=True
)


@dp.message_handler(text="ðBack")
async def bot_start(message: types.Message):
    await message.answer(f"<b>ð§ð»âð» Men Frilanserman</b>" , reply_markup=frilans)

# Buyurtmachi ----------------------------------------------------------------------------
buyurtma=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ð¸ Frilanser bilan ishlar!")
        ],
        [
            KeyboardButton(text='ð Mening buyurtmalarim'),
            KeyboardButton(text='ð¨ð»âð» Freelancer takliflar'),
        ],
        [
            KeyboardButton(text="ð¤  Mening profilim"),
            KeyboardButton(text='ð¤ Buyurtma yaratish'),

        ],
        [
            KeyboardButton(text='ð Asosiy Menyu')
        ]

    ],
    resize_keyboard=True
)
sozlamarb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Â®Men haqimdaï¸")
        ],
        [
            KeyboardButton(text="ðBack"),
            KeyboardButton(text="ð Asosiy Menyu")
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


@dp.message_handler(text="Kategoriyalar âï¸")
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
    await message.answer('Muvaffaqqiyatli amalga oshirildi â',reply_markup=frilans)
    await state.finish()






royxat = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="â Ro'yxatdan o'tish â", request_contact=True)]

    ],
    resize_keyboard=True
)

tasdiq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="â Tasdiqlash"),
            KeyboardButton(text="â Bekor qilish")
        ]
    ],
    resize_keyboard=True
)

tasdiqtaklif = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="â Xa"),
            KeyboardButton(text="â Yo'q")
        ]
    ],
    resize_keyboard=True
)


client_orqaga = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="â¬ï¸ Orqaga")
        ]
    ],resize_keyboard=True
)
frilanser_orqaga = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="â¬ï¸ orqaga")
        ]
    ],resize_keyboard=True
)

inline_tugma = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="â Tasdiqlash", callback_data='takliftasdiq'),
                      InlineKeyboardButton(text="â Bekor qilish", callback_data='taklifbekor')],
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