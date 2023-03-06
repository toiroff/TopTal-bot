from aiogram import types

from keyboards.default.kategoriya import daraja,expert_daraja,middle_daraja
from loader import dp,bot,db



@dp.message_handler(text="📊 Darajalar")
async def call(message: types.Message):
    my = db.filter_user(id=message.from_user.id)
    data = db.filter_user(id=message.from_user.id)
    if data[5] == "Middle":
        await message.answer(text="<b>Darajalar nima 🤔 ?</b>\n\n"
                                  "Darajalar bu sizni qaysi darajada ekanligingizni va ishlarni qaysi turdagi frilanser uchun ekanligini ko'rsatib beradi.\n\n"
                                  "<b>Ho'sh qanday darajamni oshiraman 🤔 ?</b>\n\n"
                                  "Siz biron ishni tugatsangiz sizga +10 bal beriladi va shunday qilib bal to'playsiz. Keyin balingiz yetgan darajaga alishtirasiz va buyurtmachi qancha ishni tugatganingizni ko'radi va sizga ishonch hosil qiladi!\n\n"
                                  "<b>Darajalar qancha bal 🤔 ?</b>\n\n"
                                  "<b>Expert - 300 bal</b>\n\n"
                                  f"Sizning darajangiz - <b>{my[5]}\n</b>"
                                  f"Siznng balingiz - <b>{my[3]}</b>\n\n"
                                  "<i>Agar darajangizni yangilamoqchi bo'lsangiz darajalardan birini tanlang !</i>",
                             reply_markup=middle_daraja)
    elif data[5] == "Expert":
        await message.answer(text="<b>Darajalar nima 🤔 ?</b>\n\n"
                                  "Darajalar bu sizni qaysi darajada ekanligingizni va ishlarni qaysi turdagi frilanser uchun ekanligini ko'rsatib beradi.\n\n"
                                  "<b>Ho'sh qanday darajamni oshiraman 🤔 ?</b>\n\n"
                                  "Siz biron ishni tugatsangiz sizga +10 bal beriladi va shunday qilib bal to'playsiz. Keyin balingiz yetgan darajaga alishtirasiz va buyurtmachi qancha ishni tugatganingizni ko'radi va sizga ishonch hosil qiladi!\n\n"
                                  f"Sizning darajangiz - <b>{my[5]}\n</b>Bu degani siz Juda kuchli frilansersiz va 30 dan ortiq buyurtmalarni topshirgansiz !\n\n"
                        
                                  "<i>Siz hozirda darajangizni yangilay olmaysiz chunki botdagi eng kotta daraja Expert !</i>",
                             reply_markup=expert_daraja)
    else:
        await message.answer(text="<b>Darajalar nima 🤔 ?</b>\n\n"
                              "Darajalar bu sizni qaysi darajada ekanligingizni va ishlarni qaysi turdagi frilanser uchun ekanligini ko'rsatib beradi.\n\n"
                              "<b>Ho'sh qanday darajamni oshiraman 🤔 ?</b>\n\n"
                              "Siz biron ishni tugatsangiz sizga +10 bal beriladi va shunday qilib bal to'playsiz. Keyin balingiz yetgan darajaga alishtirasiz va buyurtmachi qancha ishni tugatganingizni ko'radi va sizga ishonch hosil qiladi!\n\n"
                              "<b>Darajalar qancha bal 🤔 ?</b>\n\n"
                              "<b>Middle - 100 bal</b>\n"
                              "<b>Expert - 300 bal</b>\n\n"
                              f"Sizning darajangiz - <b>{my[5]}\n</b>"
                              f"Siznng balingiz - <b>{my[3]}</b>\n\n"
                              "<i>Agar darajangizni yangilamoqchi bo'lsangiz darajalardan birini tanlang !</i>",reply_markup=daraja)


@dp.message_handler(text="Middle")
async def call(message:types.Message):
    bal = db.filter_user(id=message.from_user.id)
    if bal[3] >= 100:
        db.delete_ball(ball=10,id=message.from_user.id)
        db.update_daraja(daraja='Middle',id=message.from_user.id)
        await message.answer(text="Muvaffaqqiyatli darajangiz oshirilidi. 😇✅\n\n"
                                  "Endilikda siz <b>Middle</b> darajadasiz. 🫡\n\n"
                                  "Siz endi keleajakda biron buyurtmani olishga ko'proq manfaatdorsiz !\n\n"
                                  "<i>Buyurtmachilar darajangizga juda kotta ahamiyat beradi.</i> 😎")

    else:
        await message.answer(text="Muvaffaqqiyatsizlik ❗️\n\n"
                                  "Siz tanlagan daraja uchun balingiz yetmaydi. 🫡",reply_markup=expert_daraja)

@dp.message_handler(text="Expert")
async def call(message:types.Message):
    bal = db.filter_user(id=message.from_user.id)
    if bal[3] >= 300:
        db.delete_ball(ball=10,id=message.from_user.id)
        db.update_daraja(daraja='Expert',id=message.from_user.id)
        await message.answer(text="Muvaffaqqiyatli darajangiz oshirilidi. 😇✅\n\n"
                                  "Endilikda siz <b>Expert</b> darajadasiz. 🫡\n\n"
                                  "Siz endi keleajakda biron buyurtmani olishga ko'proq manfaatdorsiz !\n\n"
                                  "<i>Buyurtmachilar darajangizga juda kotta ahamiyat beradi.</i> 😎")

    else:
        await message.answer(text="Muvaffaqqiyatsizlik ❗️\n\n"
                                  "Siz tanlagan daraja uchun balingiz yetmaydi. 🫡",reply_markup=expert_daraja)

