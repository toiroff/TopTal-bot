from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from loader import dp, bot,db
from states.states import buyrtma
from keyboards.default.menu import Buyurtma, tasdiq, buyurtma, client_orqaga, zakazdaraja


@dp.message_handler(text='📤 Buyurtma yaratish')
async def select_category(message: types.Message):
    await message.answer(f"<b>Ro'yxatdan kategoriyalarni tanlang</b>",reply_markup=Buyurtma)
    await buyrtma.project_name.set()

@dp.message_handler(state=buyrtma.project_name)
async def select_category(message: types.Message, state=FSMContext):
    project_name = message.text
    await state.update_data({'name': project_name})
    await message.answer('<b>Proektning qisqacha nomini yozing.</b>\n\nMisol uchun: <code>Telegram bot</code>, <code>WebSite</code>, <code>Application</code>, <code>Market Place</code>',reply_markup=client_orqaga)
    await buyrtma.next()

@dp.message_handler(state=buyrtma.qisqacha_nomi,text="⬅️ Orqaga")
async def bot1(message:types.Message,state:FSMContext):
    await message.answer(f"<b>👤 Men buyurtmachiman</b>" , reply_markup=buyurtma)
    await state.finish()
@dp.message_handler(state=buyrtma.qisqacha_nomi)
async def select_category(message: types.Message, state=FSMContext):
    qisqacha = message.text

    await state.update_data({'qisqacha': qisqacha})

    await message.answer("<b>Proektning ta'rifi</b>\n\nProektning funksionalligini va qancha vaqt ichida proektni bajarish mumkinligini yozing.")

    await buyrtma.next()


@dp.message_handler(state=buyrtma.project_narxi)
async def select_category(message: types.Message, state=FSMContext):
    project_narxi = message.text

    await state.update_data({'project_narxi': project_narxi})

    await message.answer("Proektning narxini kiriting\n\n<b>Iltimos faqat $ bo'lsin</b>")

    await buyrtma.next()


@dp.message_handler(state=buyrtma.phonenum)
async def select_category(message: types.Message, state=FSMContext):
    num = message.text

    await state.update_data({'phone':num})
    await message.answer('<b>Buyurtmangiz qaysi darajadagi frilanserlar uchun ?</b>🤔',reply_markup=zakazdaraja)
    await buyrtma.daraja.set()

@dp.message_handler(state=buyrtma.daraja)
async def darajas(message: types.Message,state:FSMContext):
    await state.update_data({'daraja':message.text})
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
    global daraja
    daraja = data.get('daraja')
    son = db.buyurtma_raqami()
    for s in son:
        son = s
    global jonatish

    jonatish = text=f"Buyurtma raqami #{son}\n\n" \
                                  f"Kategoriya: <b>{project_name}</b>\n\n" \
                                  f"Proektning nomi: <b>{project_nomi}</b>\n\n" \
                                  f"Proektning ta'rifi: <b>{project_tarfi}</b>\n\n" \
                                  f"Proektning narxi: <b>{project_narxi}</b>\n\n" \
                    f"Proektning darajasi: <b>{daraja}</b>\n\n"\
                    f"Frilanserlar sizning buyurtmangizni ko'rishi uchun, ✅ Tasdiqlash tugmasini bosib buyurtmangizni tasdiqlang!"

    global username
    username = message.from_user.username

    await message.answer(text=jonatish ,reply_markup=tasdiq)


    await buyrtma.tasdiqlash.set()



@dp.message_handler(state=buyrtma.tasdiqlash,text='✅ Tasdiqlash')
async def select_tasdiq(message: types.Message,state:FSMContext):

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
    await bot.send_message(chat_id="917782961", text=jonatish,reply_markup=tasdiq)
    await message.answer("Buyurtmangiz tekshiruvda ⏳, tez orada  buyurtmangiz bazaga qo'shiladi va sizga habar beriladi.",reply_markup=buyurtma)
    await state.finish()

@dp.message_handler(state=buyrtma.tasdiqlash,text='❌ Bekor qilish')
async def select_rad(message: types.Message,state:FSMContext):
    await message.answer("<b>❌ Bekor qilindi...</b>",reply_markup=buyurtma)
    await state.finish()

@dp.callback_query_handler(text="tasdiqa")
async def select_tasdiq(message: CallbackQuery,state:FSMContext):

    try:
        db.zakaz_qoshish(kategoriya=project_name,nomi=project_nomi,tarifi=project_tarfi,narxi=project_narxi,
                         user_id=idm,username=username,daraja=daraja)
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

