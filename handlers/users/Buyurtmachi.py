from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.default.menu import buyurtma, client_orqaga
from loader import dp,db,bot
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="šØš»āš» Freelancer takliflar")
async def bot_start(message: types.Message):
    try:
        user_id = message.from_user.id
        id_send = db.select_taklifs(tg_id=user_id,holat="Kutilmoqda ā³")

        for idsend in id_send:
            sql_id = idsend[6]
            data = idsend[7]

            fmalumot = db.select_royxat(id=idsend[1])
            await message.answer(f"{sql_id}\n\nš Frilanser ma'lumotlari.\n\nFrilanser name: <b>{fmalumot[2]}\n</b>Frilanser darajasi: <b>{fmalumot[5]}</b>",reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton(text="ā Tasdiqlash",
                                         callback_data=f'{data}'),
                    InlineKeyboardButton(text="ā Bekor qilish", callback_data=f'{idsend[8]}')
                ]
                ]))
        await message.answer(f"<i>Freelancer takliflar šØš»āš»</i>", reply_markup=client_orqaga)
    except:
        await message.answer('<b>Siz hali bironta taklif kiritilmadi.</b>')


@dp.message_handler(text="ā¬ļø Orqaga")
async def bot34(message: types.Message , state: FSMContext):
    await message.answer(f"<b>š¤ Men buyurtmachiman</b>", reply_markup=buyurtma)
    await state.finish()

# MENING BUYURTMALARIM _______________________________________________________________________________________________________________

@dp.message_handler(text="š Mening buyurtmalarim")
async def bots(message:types.Message):

    try:
        mal = db.zakaz_filter(user_id=message.from_user.id)
        for fr in mal:
            mal1 = fr
            ms_id = fr[0]
            inline_tugma = InlineKeyboardMarkup(
                inline_keyboard=[[InlineKeyboardButton(text="O'chirish ā", callback_data=f'buyurtmabekor')]])
            await message.answer(text=f"Buyurtma raqami #{mal1[0]}\n\n" 
                                      f"Kategoriya: <b>{mal1[4]}</b>\n\n" 
                                      f"Proektning nomi: <b>{mal1[1]}</b>\n\n" 
                                      f"Proektning ta'rifi: <b>{mal1[2]}</b>\n\n"
                                      f"Proektning darajasi: <b>{mal1[7]}</b>\n\n" 
                                     f"Proektning narxi: <b>{mal1[3]}</b>\n\n", reply_markup=inline_tugma)

        await message.answer('<i>Siz yaratgan buyurtmalaringiz</i>',reply_markup=client_orqaga)


    except:
        await message.answer('<b>Siz hali bironta buyurtma yaratmadingiz</b>')
@dp.callback_query_handler(text="buyurtmabekor")
async def call(messsage:types.CallbackQuery):

    buyurtmaid = str(messsage.message.text)
    slipt = buyurtmaid.split()
    id = slipt[1]
    data = id[7:]
    db.delete_zakaz(id=data,user_id=messsage.from_user.id)
    await messsage.answer("Muvaffaqqiyatli o'chirildi! ā",show_alert=True)
    await messsage.message.delete()

# TAKLIF TASDIQLASH _____________________________________________________________________________________________________________________

@dp.callback_query_handler(text_contains='ttasdiqlash')
async def boy_Echo(call:types.CallbackQuery):
    try:
        data = call.data.rsplit(":")
        fr_us = db.filter_user(id=data[1])
        by_us = db.filter_user(id=data[2])
        inline_tugma = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Buyurtmachi šµ", url=f"https://t.me/{fr_us[6]}")
                ],
                [
                 InlineKeyboardButton(text="Admin šØš»āš»",url="https://t.me/umarminister")
                ]
            ]
        )

        inline_buyurtmachi = InlineKeyboardMarkup(        inline_keyboard=[
                [
                    InlineKeyboardButton(text="Frilanser ", url=f"https://t.me/{by_us[6]}")
                ],
                [
                 InlineKeyboardButton(text="Admin šØš»āš»",url="https://t.me/umarminister")
                ]
            ]
        )
        db.update_taklif(holat='ā Tasdiqlash',buyurtma_id=data[4])
        await bot.send_message(chat_id=f"{data[1]}",text=f"<b>#{data[3]} Buyurtma uchun taklifingiz tasdiqlandi.</b> ā\n"
                                                   f"\n"
                                                   f"- Agar buyurtmachi uchun ishonchingiz bo'lmasa <b>Admin</b> tugmasini bosing va o'zingizni va buyurtmachini usernamenini yozib qoldirin.\n\n"
                                                   f"- Yoki o'zingiz buyurtmachi bilan ishni tugatmoqchi bo'lsangiz <b>Buyurtmachi šµ</b> tugmasini bosing.",reply_markup=inline_tugma)
        await bot.send_message(chat_id=f"{data[2]}",text=f"<b>#{data[3]} Buyurtma uchun taklif tasdiqlandi.</b> ā\n"
                                                   f"\n"
                                                   f"- Agar Frilanser uchun ishonchingiz bo'lmasa <b>Admin</b> tugmasini bosing va o'zingizni va Frilanser usernamenini yozib qoldirin. Frilanser username.\n\n"
                                                   f"- Yoki o'zingiz buyurtmachi bilan ishni tugatmoqchi bo'lsangiz <b>Buyurtmachi šµ</b> tugmasini bosing.",reply_markup=inline_buyurtmachi)
        await call.message.delete()
    except:
        await call.message.answer("Taklif tasdqilanmadi <b>Botda xatolik yuz berdi uzr so'raymiz</b>")

@dp.callback_query_handler(text_contains='tbekor')
async def boy_Echo(call:types.CallbackQuery):
    try:
        data = call.data.rsplit(":")
        fr_us = db.filter_user(id=data[1])
        by_us = db.filter_user(id=data[2])

        db.delete_taklif(Fid=data[1],tg_id=data[2],buyurtma_id=data[4])
        await bot.send_message(chat_id=f"{data[1]}",text=f"<b>#{data[3]} Buyurtma uchun taklifingiz bekor qilindi.</b> ā")

        await bot.send_message(chat_id=f"{data[2]}",text=f"<b>#{data[3]} Buyurtma uchun taklif bekor qilindi.</b> ā")

        await call.message.delete()
    except:
        await call.message.answer("Taklif bekor qilinmadi <b>Botda xatolik yuz berdi uzr so'raymiz</b>")

# FRILANSER BILAN ISHLAR ____________________________________________________________________________________________________________


@dp.message_handler(text="šø Frilanser bilan ishlar!")
async def call(message:types.Message):
    try:
        await message.answer('šø Frilanser bilan ishlaringiz \n\n'
                             "- Agar Frilanser proektni muvaffaqqiyatli tugatgan bo'lsa <b>Buyurtmani tugatish</b> tugmasini bosing!\n\n"
                             "- Agar Frilanser buyurtmani muvaffaqqiyatli bajarmagan bo'lsa <b>Buyurtmani bekor qilish</b> tugmasini bosing va frilanserga ball berilmaydi!",reply_markup=client_orqaga)
        baza=db.filterall(tg_id=message.from_user.id,holat="ā Tasdiqlash")

        for i in baza:
            data = i
            await message.answer(text=f"<b>#{data[0]} taklif</b>: Tasdiqlangan ā\n\n"
                                        f"{data[6]}\n\n", reply_markup=InlineKeyboardMarkup(
                inline_keyboard=
                [
                    [
                        InlineKeyboardButton(text="Buyurtmani tugatish !",callback_data=F'btugatish:{data[0]}'),
                    ],
                    [
                        InlineKeyboardButton(text="Buyurtmani bekor qilish ā",callback_data=f'bbekorqilish:{data[0]}')
                    ]
                ]
                 )
)


    except:
        await message.answer('Siz hali biron frilanserga ish bermadingiz!')

@dp.callback_query_handler(text_contains="btugatish")
async def call(message:types.CallbackQuery):
    try:
        rspilt = message.data.rsplit(":")
        buyurtmaid = str(message.message.text)
        slipt = buyurtmaid.split()
        taklifid = slipt[0]
        data = db.filter(id=taklifid[1:])
        id = data[1]
        db.add_ball(ball=10,id=id)
        await bot.send_message(chat_id=id,text=f"<b>#{rspilt[1]} raqamli taklifingizni muvaffaqqiyatli tugatganingiz uchun 10 ball berildi!</b>")
        db.buyurtma_bekor(id=taklifid[1:],tg_id=message.from_user.id,holat="ā Tasdiqlash")
        await message.answer("Muvaffaqqiyatli ish tugatildi\n\n"
                             "Ishni muvaffaqqiyatli tugatganingiz uchun frilanserga +10 ball berildi!", show_alert=True)
        await message.message.delete()

    except:
        await message.answer("Buyurtma bekor qilinmadi Botda xatolik yuz berdi uzr so'raymiz.",show_alert=True)

@dp.callback_query_handler(text_contains="bbekorqilish")
async def call(message:types.CallbackQuery):
    try:
        rspilt = message.data.rsplit(":")
        buyurtmaid = str(message.message.text)
        slipt = buyurtmaid.split()
        taklifid = slipt[0]
        data = db.filter(id=taklifid[1:])
        id = data[1]
        await bot.send_message(chat_id=id,
                               text=f"<b>#{rspilt[1]} raqamli taklifingizni muvaffaqqiyatsiz tugatilgani uchun bal berilmadi!</b>")
        db.buyurtma_bekor(id=taklifid[1:], tg_id=message.from_user.id, holat="ā Tasdiqlash")
        await message.answer("Muvaffaqqiyatsiz tugatildi!\n\n"
                             "Ishni muvaffaqqiyatsiz tugatganingiz uchun frilanserga ball berilmadi!", show_alert=True)
        await message.message.delete()

    except:
        await message.answer("Buyurtma bekor qilinmadi Botda xatolik yuz berdi uzr so'raymiz.", show_alert=True)
