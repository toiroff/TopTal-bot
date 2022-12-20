from aiogram import types

from keyboards.default.menu import frilans, buyurtma
from loader import dp, db


@dp.message_handler(text="📝 Mening  buyurtmalarim")
async def bot_start(message: types.Message):
    try:
        user_id = message.from_user.id
        id_send = db.select_zakaz(tg_id=user_id)
        for idsend in id_send:
            sql_id = idsend[1]
            await message.answer(f"{sql_id}",reply_markup=frilans)
    except:
        pass
    await message.answer(f"<b>Sizning buyurtmalaringiz</b>" , reply_markup=frilans)

@dp.message_handler(text="📝 Mening buyurtmalarim")
async def bot_start(message: types.Message):
    try:
        user_id = message.from_user.id
        id_send = db.select_zakaz(tg_id=user_id)
        for idsend in id_send:
            sql_id = idsend[1]
            await message.answer(f"{sql_id}",reply_markup=buyurtma)
        else:
            await message.answer("Siz hali biron buyurtma olmadingiz!")
    except:
        pass
    await message.answer(f"<b>Sizning buyurtmalaringiz</b>" , reply_markup=buyurtma)
