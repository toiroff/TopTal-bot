from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

from keyboards.default.menu import frilans, frilanser_orqaga
from keyboards.inline.creator import olish,zakazid
from loader import dp,db



@dp.message_handler(text="⬅️ orqaga")
async def cal(message:types.Message):
    await message.answer(f"<b>🧑🏻‍💻 Men Frilanserman</b>" , reply_markup=frilans)


@dp.message_handler(text="📥 Buyurtma olish")
async def bot_start(message: types.Message, ):
    await message.answer('📥 Buyurtma olish',reply_markup=frilanser_orqaga)
    kategoriya = db.filter_user(id=message.from_user.id)
    print(kategoriya[4])
    malumot = db.select_zakaz_random()
    for i in malumot:
        ms_id = i[0]
        s = i
        inline_tugma = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="Taklif kiritish", callback_data=f'taklif{ms_id}')]])
        await message.answer(text=f"Buyurtma raqami #{s[0]}\n\n" \
                                  f"Kategoriya: <b>{s[4]}</b>\n\n" \
                                  f"Proektning nomi: <b>{s[1]}</b>\n\n" \
                                  f"Proektning ta'rifi: <b>{s[2]}</b>\n\n" \
                                  f"Proektning narxi: <b>{s[3]}</b>\n\n"
                                  f"Proektning darajasi: <b>{s[7]}</b>", reply_markup=inline_tugma)

    await message.answer('<i>Tanlang</i>',reply_markup=olish)

@dp.message_handler(text="📬 Mening takliflarim")
async def bot_start(message: types.Message):
    try:
        user_id = message.from_user.id
        id_send = db.select_taklifs(Fid=user_id,holat='Kutilmoqda ⏳')
        for idsend in id_send:
            sql_id = idsend[2]
            mal = idsend
            await message.answer(f"{sql_id}\n\n<b>Holati</b>: {mal[4]}",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Taklifni bekor qilish",callback_data='taklifbekor')]]))
        await message.answer(f"<b>Sizning takliflaringiz ✅</b>", reply_markup=frilanser_orqaga)
    except:
        await message.answer(f"Siz hali biron taklif kiritmadingiz!</b>")

@dp.callback_query_handler(text="taklifbekor")
async def call(message:types.CallbackQuery):
    db.delete_taklif(Fid=message.from_user.id,holat="Kutilmoqda ⏳")
    await message.answer("Taklif o'chirildi.",show_alert=True)
    await message.message.delete()

@dp.message_handler(text='📝 Mening  buyurtmalarim')
async def bot_echo(message: types.Message, state:FSMContext):
    try:
        await message.answer('💸 Mening buyurtmalarim! \n\n'
                             "- Agar siz proektni qila olmagan bo'lsangiz <b>Buyurtmani tugatish</b> tugmasini bosing lekin sizga bal berilmaydi.",reply_markup=frilanser_orqaga)
        baza=db.filterall(Fid=message.from_user.id,holat="✅ Tasdiqlash")

        for i in baza:
            data = i
            await message.answer(text=f"{data[2]}\n\n"
                                        f"<b>#{data[0]} taklif</b>: Tasdiqlangan ✅\n\n", reply_markup=InlineKeyboardMarkup(
                inline_keyboard=
                [
                    [
                        InlineKeyboardButton(text="Buyurtmani tugatish !",callback_data='fbekorqilish'),
                    ]
                ]
                 )
                             )




    except:
        await message.answer('Siz hali biron buyurtma yaratmadingiz!')

@dp.callback_query_handler(text="fbekorqilish")
async def call(message:types.CallbackQuery):
    try:
        buyurtmaid = str(message.message.text)
        slipt = buyurtmaid.split()
        id = slipt[19]
        print(id[1:])
        db.buyurtma_bekor(id=id[1:],Fid=message.from_user.id,holat="✅ Tasdiqlash")
        await message.answer("Muvaffaqqiyatli o'chirildi! ✅",show_alert=True)
        await message.message.delete()

    except:
        await message.answer("Buyurtma bekor qilinmadi <b>Botda xatolik yuz berdi uzr so'raymiz</b>",show_alert=True)


@dp.callback_query_handler(text="keyin")
async def bot_echo(message:types.CallbackQuery):
    add = zakazid+1
    await message.message.answer('<i>Tanlang</i>',reply_markup=olish)