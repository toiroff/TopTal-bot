from aiogram.types import Message
from keyboards.default.MyProfil import *
from keyboards.default.menu import royxat, buyurtma,frilans
from loader import dp,db
from aiogram.dispatcher import FSMContext
from states.kategoriya import number,Name

@dp.message_handler(text="Mening profilim 👤")
async def my(message : Message):
    await message.reply('Mening profilim 👤',reply_markup=profilbuyurtmachi)

@dp.message_handler(text="🔙 Back")
async def b(message:Message):
    await message.answer(text="<b>👤 Men buyurtmachiman</b>",reply_markup=buyurtma)
@dp.message_handler(text="Mening ma'lumotlarim 💾")
async def mal(message:Message):
    user_id = message.from_user.id
    baza = db.filterr(id=user_id)
    # for idsend in id_send:
    #     baza = idsend[]
    await message.answer("<b>TopTal</b> Botdagi ma'lumotlaringiz\n\n\n" 
              f"<b>Telegram id</b>\n\n"
                         f" {baza[0]}\n\n" 
              f"<b>Name</b>\n\n"
                         f" {baza[2]}\n\n" 
              f"<b>Telephone</b>\n\n"
                         f" {baza[1]}\n\n"
              f"<b>Username</b>\n\n"
                         f"@{message.from_user.username}")


@dp.message_handler(text="Raqamni o'zgartirish 📞")
async def r(message: Message):
    await message.answer(text="Raqamingizni o'zgartirish uchun <b>Update Number</b> bosing!",reply_markup=royxat1)
    await number.number.set()

@dp.message_handler(state=number.number,content_types=['contact'])
async def fn(message:Message,state:FSMContext):
    await state.update_data({'number':message.contact.phone_number})
    mal = await state.get_data()
    number = mal.get('number')
    try:
      db.update_nomer(id=message.from_user.id,number=number)
    except:
        pass

    await message.answer('Muvaffaqiyatli amalga oshirildi ✅',reply_markup=profilbuyurtmachi)
    await state.finish()


@dp.message_handler(text="Ismni o'zgartirish ⬆️")
async def ism(message:Message):
    await message.answer(text="Ismingiz yoki taxallusingizni yuboring!")
    await Name.name.set()

@dp.message_handler(state=Name.name)
async def b(message:Message,state:FSMContext):
    await state.update_data({'ism':message.text})
    mal = await state.get_data()
    try:
        db.update_name(id=message.from_user.id,name=mal.get('ism'))
    except:
        pass

    await message.answer("Muvaffaqiyatli amalga oshirildi ✅",reply_markup=profilbuyurtmachi)
    await state.finish()


# Frilanser ------------------------------------------------------------

@dp.message_handler(text="👤 Mening profilim")
async def my(message : Message):
    await message.reply('Mening profilim 👤',reply_markup=profilfrilanser)

@dp.message_handler(text="💾 Mening ma'lumotlarim")
async def mal(message:Message):
    user_id = message.from_user.id
    baza = db.filterr(id=user_id)
    # for idsend in id_send:
    #     baza = idsend[]
    await message.answer("<b>TopTal</b> Botdagi ma'lumotlaringiz\n\n\n" 
              f"<b>Telegram id</b>\n\n"
                         f" {baza[0]}\n\n" 
              f"<b>Name</b>\n\n"
                         f" {baza[2]}\n\n" 
              f"<b>Telephone</b>\n\n"
                         f" {baza[1]}\n\n"
              f"<b>Username</b>\n\n"
                         f"@{message.from_user.username}\n\n"
                         f"<b>Kategoriya</b>: {baza[4]}\n\n"
                         f"<b>Daraja</b>: {baza[5]}\n\n"
                         f"<b>Balingiz</b>: {baza[3]}")

@dp.message_handler(text="Orqaga 🔙")
async def b(message:Message):
    await message.answer(text="<b>👤 Men Frilanserman</b>",reply_markup=frilans)