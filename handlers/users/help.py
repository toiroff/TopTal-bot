from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from keyboards.inline.creator import creator
from loader import dp,db


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
     await message.answer("<b>Buyruqlar:</b> \n/start - Botni ishga tushirish\n/help - Yordam")


@dp.message_handler(text="ℹ️ Nega TopTal")
async def about(message: types.Message):
    await message.answer(text="<b>Muvaffaqiyat ishlar</b>\n"
                              "Jamoalar qanday strategik ishlayotgani va birgalikda o'sishi bilan tanishing.\n\n"

                              "<b>Sharhlar</b>\n"
                              "TopTal’da hamkorlik qilish qanday ekanligini ko‘ring.\n\n"

                              "<b>Qanday qilib yollash kerak</b>\n"
                              "Ishni bajarishning turli usullari haqida bilib oling.\n\n"

                              "<b>Ishni qanday topish mumkin</b>\n"
                              "Mustaqil martaba o'sishi haqida bilib oling.", reply_markup=creator)


@dp.message_handler(text="💼 Iste'dodlar")
async def about(message: types.Message):
    await message.answer(text="<b>Development & IT</b>\n\n"

                              "<b>Design & Creative</b>\n\n"

                              "<b>Sotish & Marketing</b>\n\n"

                              "<b>Yozish & Tarjimonlik</b>\n\n"

                              "<b>Administrator & mijozlarni qo‘llab-quvvatlash</b>\n\n"

                              "<b>Moliya & buxgalteriya</b>\n\n"

                              "<b>Engineering & Architecture</b>\n\n", reply_markup=creator)