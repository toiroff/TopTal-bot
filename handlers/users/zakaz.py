from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot,db
from states.states import buyrtma
from keyboards.default.menu import Buyurtma, tasdiq,buyurtma

@dp.message_handler(text='📥 Buyurtma yaratish')
async def select_category(message: types.Message):
    await message.answer(f"<b>Ro'yxatdan kategoriyalarni tanlang</b>",reply_markup=Buyurtma)
    await buyrtma.project_name.set()

@dp.message_handler(state=buyrtma.project_name)
async def select_category(message: types.Message, state=FSMContext):
    project_name = message.text
    await state.update_data({'name': project_name})
    await message.answer('<b>Proyektning qisqacha nomini yozing.</b>\n\n<i>Misol uchun: Telegram bot, mebellar katalogi</i>')
    await buyrtma.next()


@dp.message_handler(state=buyrtma.qisqacha_nomi)
async def select_category(message: types.Message, state=FSMContext):
    qisqacha = message.text

    await state.update_data({'qisqacha': qisqacha})

    await message.answer('Proyektning qisqacha nomini, proyektning funksionalligini va qancha vaqt ichida proyektni bajarish mumkinligini yozing.')

    await buyrtma.next()


@dp.message_handler(state=buyrtma.project_narxi)
async def select_category(message: types.Message, state=FSMContext):
    project_narxi = message.text

    await state.update_data({'project_narxi': project_narxi})

    await message.answer('Proyektning narxini kiriting')

    await buyrtma.next()


@dp.message_handler(state=buyrtma.phonenum)
async def select_category(message: types.Message, state=FSMContext):
    num = message.text

    await state.update_data({'phone': num})

    data = await state.get_data()
    project_name = data.get("name")
    project_nomi = data.get("qisqacha")
    project_tarfi= data.get('project_narxi')
    project_narxi = data.get("phone")

    msg = f'Kategoriya: <b>{project_name}</b>\n\n'
    msg += f'Proyektning nomi:  <b>{project_nomi}</b>\n\n'
    msg += f"Proyektning ta'rifi: {project_tarfi}\n\n"
    msg += f'Proyektning narxi: {project_narxi} sum\n\n'

    msgss = f'Quyidagi ma`lumotlar qabul qilindi: \n\n '
    msgs = f'Kategoriya: <b>{project_name}</b>\n\n'
    msgs += f'Proyektning nomi:  <b>{project_nomi}</b>\n\n'
    msgs += f"Proyektning ta'rifi: {project_tarfi}\n\n"
    msgs += f'Proyektning narxi: {project_narxi} sum\n\n'

    msgs += f"<i>Frilanserlar sizning buyurtmangizni ko'rishi uchun, ✅ Tasdiqlash tugmasini bosib buyurtmangizni tasdiqlang!</i>"

    global user
    user = f"{msg}"
    await message.answer(msgss)
    await message.answer(msgs, reply_markup=tasdiq)


    await state.finish()



@dp.message_handler(text='✅ Tasdiqlash')
async def select_tasdiq(message: types.Message):
    try:
        user_id = message.from_user.id
        db.zakaz_qoshish(zakaz=user,
                         tg_id=user_id)
    except Exception as xatolik:
        print(xatolik)

    await bot.send_message(chat_id=917782961, text=user)

    await message.answer("Buyurtmanigiz bazaga saqlandi, tez orada  frilanserlar siz bilan bot orqali bog'lanadi.",reply_markup=buyurtma)


@dp.message_handler(text='❌ Bekor qilish')
async def select_rad(message: types.Message):
    await message.answer("<b>❌ Bekor qilindi...</b>",reply_markup=buyurtma)