from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from keyboards.default.menu import buyurtma, inline_tugma2
from loader import dp,db,bot
from aiogram.dispatcher import FSMContext
from .taklif1 import bot_echo
@dp.message_handler(text="✅ Freelancer takliflar")
async def bot_start(message: types.Message):
    try:
        user_id = message.from_user.id
        id_send = db.select_taklifs(tg_id=user_id)
        for idsend in id_send:
            sql_id = idsend[2]
            await message.answer(f"{sql_id}",reply_markup=inline_tugma2)
    except:
        pass
    await message.answer(f"<b>✅ Freelancer takliflar 👆👆👆</b>" , reply_markup=buyurtma)

@dp.message_handler(text="📜 Mening buyurtmalarim")
async def bots(message:types.Message):

    try:
        mal = db.filter_zakaz(user_id=message.from_user.id)
        for fr in mal:
            mal1 = fr
            ms_id = fr[0]
            inline_tugma = InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text="O'chirish ❌", callback_data=f'taklif{ms_id}')]])
            await message.answer(text=f"Buyurtma raqami # {mal1[0]}\n\n" 
                                      f"Kategoriya: {mal1[4]}\n\n" 
                                      f"Proyektning nomi: {mal1[1]}\n\n" 
                                      f"Proyektning ta'rifi: {mal1[2]}\n\n" 
                                     f"Proyektning narxi: {mal1[3]} sum\n\n", reply_markup=inline_tugma)

        else:
            await message.answer('<b>Siz hali bironta buyurtma yaratmadingiz</b>')



    except:
        pass

@dp.callback_query_handler(text="takliftasdiqlash")
async def bot1(messgae: CallbackQuery, state:FSMContext):
    mal = await state.get_data()
    idm = mal.get('idm')
    ms_us = mal.get('ms_us')
    inline_tugma = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Frilanserga Aloqa", url=f"https://t.me/{ms_us}")]])
    inline_tugma2 = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="Frilanserga Aloqa", url=f"https://t.me/{messgae.from_user.id}")]])
    await messgae.message.edit_text("<b>Buyurtma tasdiqlandi !</h>\n\n"
                             "- Buyurtmani o'zingiz frilanser bilan ishni tugatmoqchi bo'lsangiz <i>Frilanserga aloqa</i> tugmasini bosing\n\n"
                            "- Frilanserga ishonchingiz bo'lmasa admin bilan buyurtmani tugatishingiz mumkin.Agar admin bilan qilmoqhi bo'lsangiz @UmarMinister ga frilanserni id yoki usernameni yuboring !",reply_markup=inline_tugma)
    await bot.send_message(text="<b>Buyurtmachi siz topshirgan taklifni tasdiqladi !</b>\n\n"
                                    "- Buyurtmani o'zingiz buyurtmachi bilan ishni tugatmoqchi bo'lsangiz <i>Buyurtmachiga aloqa</i> tugmasini bosing\n\n"
                            "- Buyurtmachiga ishonchingiz bo'lmasa admin bilan buyurtmani tugatishingiz mumkin.Agar admin bilan qilmoqhi bo'lsangiz @UmarMinister ga buyurtmachini id yoki usernameni yuboring !",reply_markup=inline_tugma2)
