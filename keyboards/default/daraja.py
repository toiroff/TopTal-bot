from aiogram import types
from aiogram.types import Message
from states.states import *
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
from loader import dp,db,bot


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
            KeyboardButton(text="1-daraja"),
            KeyboardButton(text="2-daraja"),
            KeyboardButton(text="3-daraja")
        ],
        [
            KeyboardButton(text="4-daraja"),
            KeyboardButton(text="5-daraja"),
            KeyboardButton(text="🔙 Orqaga")
        ]
    ],resize_keyboard=True
)
# Backend Menu --------------------------------------------------
daraja1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧲Django bo'yicha tajriba")
        ],
        [
            KeyboardButton(text="🤖 Telegram bo'yicha tajriba"),
            KeyboardButton(text="🔙 Orqaga")

        ]
    ],resize_keyboard=True
)
@dp.message_handler(text="📈 Tajriba oshirish")
async def daraja(message : Message):
    await message.answer(text="Yo'nalish tanlang va mashqlardan muvaffaqqiyatli o'ting",reply_markup=darajamenu)

@dp.message_handler(text="Back-end")
async def botss(message: Message):
    await message.answer("Yo'nalish tanlang va mashqlardan muvaffaqqiyatli o'ting✅",reply_markup=backmenu)
    await start.entry.set()

@dp.message_handler(state=start.entry,text="1-daraja")
async def j(message : Message,state:FSMContext):
    bal = db.select_bal(id=message.from_user.id)
    daraja = db.select_daraja(id=message.from_user.id)
    await message.answer(text=f"Muvaffaqiyatli tanlandi✅ \n\n💵Sizning balingiz : {bal[3]}\n\n📊Darajangiz : {daraja[5]}")
    await message.answer(text="O'zingizga yoqgan yo'nalishni tanlang",reply_markup=daraja1)
    await start.daraja1.set()

@dp.message_handler(state=start.daraja1,text="🧲Django bo'yicha tajriba")
async def bots(message : Message,state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id,text="<b>Sizga biz O'zingiz uchun Portfolio saytining Front-end qismini beramiz va siz Back-end bilan bog'lab sayt yaratasiz</b>\n\n"
                                                             "<i> Bajarib bo'lgach botni kodini shu xabardan keyin yuboring va adminlar tekshirib sizning balingiz va darajangizni juniorga ko'tarishadi \nBu darajaga buyurtmachilar ko'p ahamiyat berishadi va sizga ish berish imkoniyati ortadi.</i>")
    await bot.send_document(chat_id=message.from_user.id,document='https://t.me/UMARForever/46')
    await bot.send_message(chat_id=message.from_user.id,text="Siz xatolarga uchrashingizni bilamiz va shuning uchun Back-end + Front-end qismini beramiz siz bundan shablon sifatida bog'lanasiz")
    await bot.send_document(chat_id=message.from_user.id,document="https://t.me/MistrUz/43")
    await state.finish()
@dp.message_handler(state=start.daraja1, text="🤖 Telegram bo'yicha tajriba")
async def j(message : Message, state: FSMContext):
    await message.answer('<b>Sizga biz @Frilanser_Robot kodini beramiz va siz undan shablon sifatida foydalanib bot yaratasiz.</b>\n\n'
                         "<i> Bajarib bo'lgach botni kodini shu xabardan keyin yuboring va adminlar tekshirib sizning balingiz va darajangizni juniorga ko'tarishadi \nBu darajaga buyurtmachilar ko'p ahamiyat berishadi va sizga ish berish imkoniyati ortadi.</i>")
    await bot.send_document(chat_id=message.from_user.id,document="https://t.me/UMARForever/43")
    await state.finish()

# DARAJA 2----------------------------------------------------------------------------------------
@dp.message_handler(state=start.entry,text="2-daraja")
async def j(message: Message, state: FSMContext):
    bal = db.select_bal(id=message.from_user.id)
    daraja = db.select_daraja(id=message.from_user.id)
    await message.answer(text=f"Muvaffaqiyatli tanlandi✅ \n\n💵Sizning balingiz : {bal[3]}\n\n📊Darajangiz : {daraja[5]}",reply_markup=daraja1)
    await start.daraja2.set()

@dp.message_handler(state=start.daraja2,text="🧲Django bo'yicha tajriba")
async def django(message:Message,state:FSMContext):
    await bot.send_message(chat_id=message.from_user.id,text="<b>Bu daraja 1-darajadan qiyinroq bo'lib sizga biz Marga saytnini Front-end qismini beramiz 😃</b>\n\n"
                                                             "<i> Bajarib bo'lgach botni kodini shu xabardan keyin yuboring va adminlar tekshirib sizning balingiz va darajangizni juniorga ko'tarishadi \nBu darajaga buyurtmachilar ko'p ahamiyat berishadi va sizga ish berish imkoniyati ortadi.</i>")
    await bot.send_document(message.from_user.id,document="https://t.me/UMARForever/47")
    await state.finish()
@dp.message_handler(state=start.entry,text="3-daraja")
async def j(message: Message, state: FSMContext):
    bal = db.select_bal(id=message.from_user.id)
    daraja = db.select_daraja(id=message.from_user.id)
    await message.answer(text=f"Muvaffaqiyatli tanlandi✅ \n\n💵Sizning balingiz : {bal[3]}\n\n📊Darajangiz : {daraja[5]}")
    await state.finish()
@dp.message_handler(state=start.entry, text="4-daraja")
async def j(message: Message, state: FSMContext):
    bal = db.select_bal(id=message.from_user.id)
    daraja = db.select_daraja(id=message.from_user.id)
    await message.answer(text=f"Muvaffaqiyatli tanlandi✅ \n\n💵Sizning balingiz : {bal[3]}\n\n📊Darajangiz : {daraja[5]}")
    await state.finish()
@dp.message_handler(state=start.entry, text="5-daraja")
async def j(message: Message, state: FSMContext):
    bal = db.select_bal(id=message.from_user.id)
    daraja = db.select_daraja(id=message.from_user.id)
    await message.answer(text=f"Muvaffaqiyatli tanlandi✅ \n\n💵Sizning balingiz : {bal[3]}\n\n📊Darajangiz : {daraja[5]}")
    await state.finish()
@dp.message_handler(state=start.entry,text="🔙 Orqaga")
async def bots(message :Message,state:FSMContext):
    await message.answer("Yo'nalish tanlang va mashqlardan muvaffaqqiyatli o'ting✅",reply_markup=darajamenu)
    await state.finish()
    # await message.answer("<b>Sizga biz O'zingiz uchun Portfolio saytining Front-end qismini beramiz va siz Back-end bilan bog'lab sayt yaratasiz</b>")



@dp.message_handler(text="Men haqimda®️")
async def menku(message : Message):
    bid = db.select_daraja(id=message.from_user.id)
    await message.answer(f"TopTal botdagi FREELANCER ma'lumotlar\n\n"
                         f"<b> 🆔 raqamingiz </b> : {bid[0]}\n"
                         f"<b> 📞 Telefon </b>: {bid[1]}\n"
                         f"<b> ☑ Kategoriya</b>: {bid[4]}\n"
                         f"<b> 📊 Daraja </b>:{bid[5]}")