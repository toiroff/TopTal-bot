from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp, bot,db
from states.states import *
from keyboards.default.menu import *


@dp.callback_query_handler()
async def bot_echo(message:types.Message,state:FSMContext):
        user_id = message.from_user.id
        malumot = message.data
        useer=message.from_user.username
        ms_id = malumot[6:]
        print(ms_id)
        print(useer)

        await state.update_data({'ms_id': ms_id})
        await bot.send_message(chat_id=user_id,text="<b>Aynan qanday yo'l bilan bu topshiriqni yechishingizni izohlang.</b>\n\n<i>Iltimos izohingizni koproq va tushunarli qoldiring</i>\n\n Diqqat Har bir malumotni to'g'ri kiriting keyn tushunmovchilik bo'lmaslik uchun",reply_markup=frilans)
        await taklif.taklif.set()

@dp.message_handler(state=taklif.taklif)
async def select_category(message: types.Message, state=FSMContext):
    tx = message.text
    await state.update_data({'txt': tx})
    await message.answer('<b>Proyektning narxini kiritng.</b>')
    await taklif.narxi.set()

    @dp.message_handler(state=taklif.narxi)
    async def select_category(message: types.Message, state=FSMContext):
        project_narx = message.text
        await state.update_data({'sum': project_narx})
        await message.answer('<b>Taklif qabul qilinsa kimga murojat qilinsin tahminan mana bunday hoatda kiritng, iltimos faqat shu holatda kiriting👇🏻👇🏻👇🏻</b>\n\n<code>@MistrUz</code>')
        await taklif.aloqa.set()

@dp.message_handler(state=taklif.aloqa)
async def select_category(message: types.Message, state=FSMContext):
    aloqa = message.text
    await state.update_data({'aloqa': aloqa})
    user_id = message.from_user.id
    malumot= await state.get_data()

    takliff = malumot.get("txt")
    narxi = malumot.get("sum")
    ms_id = malumot.get('ms_id')
    alo = malumot.get("aloqa")
    ms_us = alo[1:]
    ekranga_chiqarish =  f"<b>Taklifingiz:</b> {takliff}\n\n" \
                        f"<b>Proyektning narxi:</b> {narxi}\n"


    await bot.send_message(chat_id=user_id,text=f"To'g'ri taklif kiritgan bo'lsangiz  ✅ Xa tugmasini bosing\n\n{ekranga_chiqarish}",reply_markup=tasdiqtaklif)
    await taklif.tasdiqlash.set()


@dp.message_handler(state=taklif.tasdiqlash,text="✅ Xa")
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.chat.username
    user_id = message.from_user.id
    malumot = await state.get_data()

    takliff = malumot.get("txt")
    narxi = malumot.get("sum")
    ms_id = malumot.get('ms_id')
    alo = malumot.get("aloqa")
    ms_us = alo[1:]
    ekranga_chiqarish = f"{takliff}\n\n" \
                        f"<b>Proyektning narxi:</b> {narxi}"
    try:
        id_send = db.select_taklif(id=ms_id)
        for idsend in id_send:
            sql_id = idsend[2]

            db.taklif_qoshish(Tid=message.from_user.id,
                              zakaz=f"#{ms_id} Buyurtma uchun taklif\n\n{ekranga_chiqarish}\n\n<b>Frilanserga Aloqa : </b> @{ms_us}", tg_id=sql_id)
            inline_tugma = InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text="Frilanserga Aloqa", url=f"https://t.me/{ms_us}")]])
            await bot.send_message(chat_id=sql_id, text=f"#{ms_id} Buyurtmangiz uchun taklif\n\n{ekranga_chiqarish}",reply_markup=inline_tugma)
    except:
        pass
    await bot.send_message(chat_id=user_id,text=f"#{ms_id} <b>Buyurtma bo'yicha taklif buyurtmachiga yuborildi</b>\n\n<i>Taklifingizni Buyurtmachi qabul qilsa sizga aloqa o'rnatadi.</i>",reply_markup=frilans)
    await state.finish()

@dp.message_handler(state=taklif.tasdiqlash,text="❌ Yo'q")
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.text
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Bekor qilindi ❌",reply_markup=frilans)
    await state.finish()

