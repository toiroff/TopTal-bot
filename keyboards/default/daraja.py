from aiogram.types import Message
from states.states import *
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
from loader import dp,db


darajamenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Back-end"),
            KeyboardButton(text="Front-end")
        ],
        [
            KeyboardButton(text="Full-Stack"),
            KeyboardButton(text="🔝 Asosiy Menyu")
        ],
    ],resize_keyboard=True
)
backmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Junior"),
            KeyboardButton(text="Middle")
        ],
        [
            KeyboardButton(text="Senior"),
            KeyboardButton(text="🔙 Orqaga")
        ]
    ],resize_keyboard=True
)
@dp.message_handler(text="📈 Daraja oshirish")
async def daraja(message : Message):
    await message.answer(text="Yo'nalish tanlang va mashqlardan muvaffaqqiyatli o'ting",reply_markup=darajamenu)

@dp.message_handler(text="Back-end")
async def bot(message: Message):
    await message.answer("Yo'nalish tanlang va mashqlardan muvaffaqqiyatli o'ting✅",reply_markup=backmenu)
    await start.entry.set()


@dp.message_handler(state=start.entry,text="Junior")
async def j(message : Message,state:FSMContext):
    bal = db.select_bal(id=message.from_user.id)
    await message.answer(text=f"Muvaffaqiyatli tanlandi✅ \n\nSizning balingiz : {bal[3]}")

    await state.finish()

@dp.message_handler(state=start.entry,text="Middle")
async def j(message: Message, state: FSMContext):
    bal = db.select_bal(id=message.from_user.id)
    await message.answer(text=f"Muvaffaqiyatli tanlandi✅ \n\nSizning balingiz : {bal[3]}")
    await state.finish()

@dp.message_handler(state=start.entry,text="Senior")
async def j(message: Message, state: FSMContext):
    bal = db.select_bal(id=message.from_user.id)
    await message.answer(text=f"Muvaffaqiyatli tanlandi✅ \n\nSizning balingiz : {bal[3]}")

    await state.finish()




