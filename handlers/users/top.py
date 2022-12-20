from aiogram import types
from aiogram.dispatcher import FSMContext
from states.states import topish
from loader import dp,db
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
# Echo bot


@dp.message_handler(text='🔎 Buyurtmani toping')
async def bot_echo(message: types.Message,state:FSMContext):
        await message.answer('Buyurtma id kiriting')
        await topish.buyurtma_topish.set()

@dp.message_handler(state=topish.buyurtma_topish)
async def bot_echo(message: types.Message, state: FSMContext):
        top = message.text
        await state.update_data({'top': top})
        malumot = await state.get_data()
        topish = malumot.get('top')

        malumot = db.filter(id=topish)

        malumot1 = db.select_random_zakaz()
        print(malumot)
        for s in malumot1:
            ms_id = s[0]
            inline_tugma = InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text="Taklif kiritish", callback_data=f'taklif{ms_id}')]])

        await message.answer(text=f"Buyurtma raqami # {malumot[0]}\n\n" \
                                      f"Kategoriya: {malumot[4]}\n\n" \
                                      f"Proyektning nomi: {malumot[1]}\n\n" \
                                      f"Proyektning ta'rifi: {malumot[2]}\n\n" \
                                      f"Proyektning narxi: {malumot[3]} sum\n\n",reply_markup=inline_tugma)
        await state.finish()
