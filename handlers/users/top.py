from aiogram import types
from aiogram.dispatcher import FSMContext
from states.states import topish
from loader import dp,db
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
# Echo bot


@dp.message_handler(text='🔎 Search')
async def bot_echo(message: types.Message,state:FSMContext):
        await message.answer('Buyurtma id kiriting')
        await topish.buyurtma_topish.set()

@dp.message_handler(state=topish.buyurtma_topish)
async def bot_echo(message: types.Message, state: FSMContext):
        top = message.text
        await state.update_data({'top': top})
        mal = await state.get_data()
        topish = mal.get('top')
        try:
            malumot = db.filter_zakaz(id=topish)
            inline_tugma = InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text="Taklif kiritish", callback_data=f'taklif{malumot[0]}')]])
            await message.answer(text=f"Buyurtma raqami #{malumot[0]}\n\n" \
                                      f"Kategoriya: <b>{malumot[4]}</b>\n\n" \
                                      f"Proyektning nomi: <b>{malumot[1]}</b>\n\n" \
                                      f"Proyektning ta'rifi: <b>{malumot[2]}</b>\n\n" \
                                      f"Proyektning narxi: <b>{malumot[3]}</b>\n\n",reply_markup=inline_tugma)
        except :
            await message.answer('<b>Bu id raqamdagi buyurtma mavjud emas!</b>')

        await state.finish()
