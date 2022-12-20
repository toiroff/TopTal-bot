from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
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

    await state.update_data({'phone':num})
    await state.update_data({'id':message.from_user.id})
    data = await state.get_data()
    global project_name
    project_name = data.get("name")
    global project_nomi
    project_nomi = data.get("qisqacha")
    global project_tarfi
    project_tarfi= data.get('project_narxi')
    global project_narxi
    project_narxi = data.get("phone")
    son = db.buyurtma_raqami()
    for s in son:
        son = s
    global jonatish
    jonatish = f"Buyurtma ID : {son}"\
               f"Kategoriya: {project_name}\n" \
               f"Proyektning nomi: {project_nomi}\n" \
               f"Proyektning ta'rifi: {project_tarfi}\n" \
               f"Proyektning narxi: {project_narxi} sum\n\n" \
               f"Frilanserlar sizning buyurtmangizni ko'rishi uchun, ✅ Tasdiqlash tugmasini bosib buyurtmangizni tasdiqlang!"



    # await message.answer(text=jonatish,  reply_markup=InlineKeyboardMarkup( inline_keyboard=[
    #                              [ InlineKeyboardButton('Taklif Kiritish',callback_data=f"inline {son}",)
#         ]
#     ]
# )
#                          )

    await message.answer(text=jonatish ,reply_markup=tasdiq)


    await buyrtma.tasdiqlash.set()



@dp.message_handler(state=buyrtma.tasdiqlash,text='✅ Tasdiqlash')
async def select_tasdiq(message: types.Message,state:FSMContext):
    data = await state.get_data()
    project_name = data.get("name")
    project_nomi = data.get("qisqacha")
    project_tarfi= data.get('project_narxi')
    project_narxi = data.get("phone")
    id = data.get('id')
    son = db.buyurtma_raqami()
    print(project_name)
    tasdiq = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Tasdiqlash",callback_data="tasdiqa")
            ],
            [
                InlineKeyboardButton(text="❌ Bekor qilish",callback_data="bekora")
            ]
        ]
    )

    global idm

    idm = message.from_user.id
    # global idm
    await bot.send_message(chat_id=917782961, text=jonatish,reply_markup=tasdiq)
    await message.answer("Buyurtmanigiz bazaga saqlandi, tez orada  frilanserlar siz bilan bot orqali bog'lanadi.",reply_markup=buyurtma)
    await state.finish()

@dp.message_handler(state=buyrtma.phonenum,text='❌ Bekor qilish')
async def select_rad(message: types.Message,state:FSMContext):
    await message.answer("<b>❌ Bekor qilindi...</b>",reply_markup=buyurtma)
    await state.finish()

@dp.callback_query_handler(text="tasdiqa")
async def select_tasdiq(message: CallbackQuery,state:FSMContext):
    # data = await state.get_data()
    # project_name = data.get("name")
    # project_nomi = data.get("qisqacha")
    # project_tarfi = data.get('project_narxi')
    # project_narxi = data.get("phone")

    try:
        user_id = message.from_user.id
        db.zakaz_qoshish(kategoriya=project_name,nomi=project_nomi,tarifi=project_tarfi,narxi=project_narxi,
                         user_id=idm)
    except Exception as xatolik:
        print(xatolik)
    await bot.send_message(chat_id=idm,text="Buyurtmanigiz bazaga saqlandi, tez orada  frilanserlar siz bilan bot orqali bog'lanadi.",reply_markup=buyurtma)
    await message.message.delete()

@dp.callback_query_handler(text="bekora")
async def select_rad(message: CallbackQuery):
    await bot.send_message(chat_id=idm,text="<b>❌ Buyurtmangiz bekor qilindi...</b>\n"
                         "Agar biron xatolik bo'lgan bo'lsa @UmarMinister yozishingiz mumkin",reply_markup=buyurtma)
    await message.answer(text="❌ Bekor qilindi...")
    await message.message.delete()

