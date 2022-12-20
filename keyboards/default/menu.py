from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from keyboards.default.kategoriya import soxa
from loader import dp,db
from states.kategoriya import kategoriya

menuuz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧑🏻‍💻 Men Frilanserman"),
            KeyboardButton(text="👤 Men buyurtmachiman")
        ],
        [
            KeyboardButton(text="📈 Tajriba oshirish"),
            KeyboardButton(text="💎 Bal Nima ?")
        ],
        [
            KeyboardButton(text="💼 Iste'dodlar"),
            KeyboardButton(text="  ℹ️ Nega TopTal")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="🧑🏻‍💻 Men Frilanserman")
async def bot_start(message: types.Message):
    await message.answer(f"<b>🧑🏻‍💻 Men Frilanserman</b>" , reply_markup=frilans)
@dp.message_handler(text="👤 Men buyurtmachiman")
async def bot_start(message: types.Message):
    await message.answer(f"<b>👤 Men buyurtmachiman</b>" , reply_markup=buyurtma)
@dp.message_handler(text="🔝 Asosiy Menyu")
async def bot_start(message: types.Message):
    await message.answer(f"🔝 <b>Asosiy Menyu</b>" , reply_markup=menuuz)


frilans = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Mening  buyurtmalarim"),
         KeyboardButton(text='📥 Buyurtma olish')
        ],
        [
            KeyboardButton(text='✅ Mening takliflarim'), KeyboardButton(text='🔎 Buyurtmani toping'),
        ],
        [
            KeyboardButton(text="⚙️ Sozlamalar")
        ],
        [KeyboardButton(text='🔝 Asosiy Menyu')]
    ],
    resize_keyboard=True
)

sozlamar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Men haqimda®️")
        ],
        [
            KeyboardButton(text="Kategoriyalar ☑️"),

        ],
        [
            KeyboardButton(text="🔙Back"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ]
    ],resize_keyboard=True
)
@dp.message_handler(text="🔙Back")
async def bot_start(message: types.Message):
    await message.answer(f"<b>🧑🏻‍💻 Men Frilanserman</b>" , reply_markup=frilans)

# Buyurtmachi ----------------------------------------------------------------------------
buyurtma=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📝 Mening buyurtmalarim'),KeyboardButton(text='📥 Buyurtma yaratish')],
        [KeyboardButton(text='✅ Freelancer takliflar')],
        [
            KeyboardButton(text="Sozlamalar⚙")
        ],[KeyboardButton(text='🔝 Asosiy Menyu')]

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

@dp.message_handler(text="⚙️ Sozlamalar")
async def bot_start(message: types.Message):
    await message.answer(f"<b>⚙️ Sozlamalar</b>" , reply_markup=sozlamar)


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



@dp.message_handler(text="Raqamni o'zgartirish")
async def bot_start(message: types.Message):
    await message.answer(f"<b>Tez kunda...</b>" , reply_markup=sozlamar)


nomer_update = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="☎️ Telfon jo'nating", request_contact=True)]

    ],
    resize_keyboard=True
)


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