from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from states.ochirish import kategoriya
from keyboards.default.menu import menuuz
from loader import dp,db


# Echo bot
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
                InlineKeyboardButton(text="Buyurtmani ochirish",callback_data='til')
            ]
        ]
    )
                         )

    await message.answer(text='Tanlang',reply_markup=menuuz)

    # for s in baza:
    #
    #
    #
    #     await message.answer(text=f"Buyurtma raqami # {baza[0]}\n\n" \
    #                           f"Kategoriya: {baza[4]}\n\n" \
    #                           f"Proyektning nomi: {baza[1]}\n\n" \
    #                           f"Proyektning ta'rifi: {baza[2]}\n\n" \
    #                           f"Proyektning narxi: {baza[3]} sum\n\n",)
    # await state.finish()
