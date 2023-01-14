from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

from keyboards.default.menu import frilans, menuuz
from keyboards.inline.creator import olish
from loader import dp,db




@dp.message_handler(text="📥 Buyurtma olish")
async def bot_start(message: types.Message, ):
    malumot = db.select_random_zakaz()
    print(malumot)
    for s in malumot:
        ms_id = s[0]
        inline_tugma = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="Taklif kiritish", callback_data=f'taklif{ms_id}')]])
        await message.answer(text=f"Buyurtma raqami # {s[0]}\n\n" \
                                  f"Kategoriya: {s[4]}\n\n" \
                                  f"Proyektning nomi: {s[1]}\n\n" \
                                  f"Proyektning ta'rifi: {s[2]}\n\n" \
                                  f"Proyektning narxi: {s[3]} sum\n\n", reply_markup=inline_tugma)

    await message.answer('<i>Tanlang</i>',reply_markup=olish)

@dp.message_handler(text="✅ Mening takliflarim")
async def bot_start(message: types.Message):
    try:
        user_id = message.from_user.id
        id_send = db.select_taklifs(Tid=user_id)
        for idsend in id_send:
            sql_id = idsend[2]
            print((sql_id))
            mal = idsend
            await message.answer(f"{sql_id}\n\n<b>Holati</b>\n\n{mal[4]}",reply_markup=frilans)
    except:
        pass
    await message.answer(f"<b>✅ Sizning takliflaringiz 👆👆👆</b>" , reply_markup=frilans)

@dp.message_handler(text='📝 Mening  buyurtmalarim')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='📝 Mening  buyurtmalarim')
    baza=db.filter(user_id=message.from_user.id)


    await message.answer(text=f"Buyurtma raqami # {baza[0]}\n\n" \
                                  f"Kategoriya: {baza[4]}\n\n" \
                                  f"Proyektning nomi: {baza[1]}\n\n" \
                                  f"Proyektning ta'rifi: {baza[2]}\n\n" \
                                  f"Proyektning narxi: {baza[3]} sum\n\n", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                InlineKeyboardButton(text="Buyurtmani bekor qilish",callback_data='til')
            ]
        ]
    )
                         )

    await message.answer(text='Tanlang',reply_markup=frilans)

