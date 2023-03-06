import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot,db
from states.states import *
from keyboards.default.menu import *




@dp.callback_query_handler()
async def bot_echo1(message:types.CallbackQuery,state:FSMContext):
    user_id = message.from_user.id
    zakaz = message.message.text
    await state.update_data({'zakaz':zakaz})
    malumot = message.data
    print(malumot)
    await state.update_data({'malumot':malumot})
    ms_id = malumot[6:]

    await state.update_data({'ms_id': ms_id})
    await bot.send_message(chat_id=user_id,text="<b>Aynan qanday yo'l bilan bu topshiriqni yechishingizni izohlang.</b>\n\n<i>Iltimos izohingizni koproq va tushunarli qoldiring</i>\n\n Diqqat Har bir malumotni to'g'ri kiriting keyn tushunmovchilik bo'lmaslik uchun",reply_markup=frilanser_orqaga)
    await taklif.taklif.set()

@dp.message_handler(state=taklif.taklif,text="⬅️ orqaga")
async def cal(message:types.Message,state:FSMContext):
    await message.answer(f"<b>🧑🏻‍💻 Men Frilanserman</b>" , reply_markup=frilans)
    await state.finish()
@dp.message_handler(state=taklif.taklif)
async def select_category(message: types.Message, state=FSMContext):
    tx = message.text
    await state.update_data({'txt': tx})
    await message.answer('<b>Proektning narxini kiritng.\n\nIltimos $ kiriting!</b>')
    await taklif.narxi.set()

    @dp.message_handler(state=taklif.narxi)
    async def select_category(message: types.Message, state=FSMContext):
        project_narx = message.text
        await state.update_data({'sum': project_narx})
        await message.answer('<b>Taklif qabul qilinsa kimga murojat qilinsin tahminan mana bunday hoalda kiritng, iltimos faqat shu holatda kiriting👇🏻👇🏻👇🏻</b>\n\n<code>@UmarDeveloper</code>')
        await taklif.aloqa.set()

@dp.message_handler(state=taklif.aloqa)
async def select_category(message: types.Message, state=FSMContext):
    aloqa = message.text
    await state.update_data({'aloqa': aloqa})
    user_id = message.from_user.id
    malumot= await state.get_data()

    takliff = malumot.get("txt")
    narxi = malumot.get("sum")
    alo = malumot.get("aloqa")
    ekranga_chiqarish =  f"Taklifingiz: <b>{takliff}</b>\n\n" \
                        f"Proektning narxi:<b>{narxi}</b>\n"


    await bot.send_message(chat_id=user_id,text=f"To'g'ri taklif kiritgan bo'lsangiz  ✅ Xa tugmasini bosing\n\n{ekranga_chiqarish}",reply_markup=tasdiqtaklif)
    await taklif.tasdiqlash.set()


@dp.message_handler(state=taklif.tasdiqlash,text="✅ Xa")
async def bot_echo(message: types.Message, state: FSMContext):
    txt = message.chat.username
    user_id = message.from_user.id
    malumot = await state.get_data()
    takliff = malumot.get("txt")
    narxi = malumot.get("sum")
    ms_id = malumot.get('ms_id')
    alo = malumot.get("aloqa")
    ms_us = alo[1:]
    zakaz = malumot.get('zakaz')

    await state.update_data({'ms_us':ms_us})
    ekranga_chiqarish = f"<b>{takliff}</b>\n\n" \
                        f"Proektning narxi: <b>{narxi}</b>"
    a = 1
    b = 100
    r = random.uniform(a,b)
    id_send = db.select_taklif1(id=ms_id)
    for idsend in id_send:
        sql_id = idsend[5]
        inline_tugma2 = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="✅ Tasdiqlash", callback_data=f'ttasdiqlash:{message.from_user.id}:{sql_id}:{ms_id}:{r}'),
                              InlineKeyboardButton(text="❌ Bekor qilish",callback_data=f'tbekor:{message.from_user.id}:{sql_id}:{ms_id}:{r}')],
                             ])

# Taklif bazaga qo'shilishi _______________________________________________________________________________________________________

        db.taklif_qoshish(data=f'ttasdiqlash:{message.from_user.id}:{sql_id}:{ms_id}:{r}',deletedata=f'tbekor:{message.from_user.id}:{sql_id}:{ms_id}:{r}',Fid=message.from_user.id,zakaz=zakaz,
                          taklif=f"#{ms_id} Buyurtma uchun taklif\n\n{ekranga_chiqarish}\n\nFrilanserga Aloqa: <b>@{ms_us}</b>", tg_id=sql_id,holat='Kutilmoqda ⏳',buyurtma_id=r)

# Taklif buyurtmachiga borishi ___________________________________________________________________________________________________8
        fmalumot = db.select_royxat(id=message.from_user.id)
        await bot.send_message(chat_id=sql_id, text=f"#{ms_id} Buyurtmangiz uchun taklif\n\n{ekranga_chiqarish}\n\n📑 Frilanser ma'lumotlari.\n\nFrilanser name: <b>{fmalumot[2]}\n</b>Frilanser darajasi: <b>{fmalumot[5]}</b>",reply_markup=inline_tugma2)

    await bot.send_message(chat_id=user_id,text=f"#{ms_id} <b>Buyurtma bo'yicha taklif buyurtmachiga yuborildi</b>\n\n<i>Taklifingizni Buyurtmachi qabul qilsa sizga aloqa o'rnatadi.</i>",reply_markup=frilans)
    await state.finish()

@dp.message_handler(state=taklif.tasdiqlash,text="❌ Yo'q")
async def bot_echo2(message: types.Message, state: FSMContext):
    txt = message.text
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id,text="Bekor qilindi ❌",reply_markup=frilans)
    await state.finish()


