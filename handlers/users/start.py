from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.creator import olish
from loader import dp, db, bot
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default.menu import menuuz,royxat,buyurtma,frilans


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        id =message.from_user.id
        nomer = db.select_royxat(id=id)
        if nomer[1] == message.contact:
            pass

        else:
            await message.answer("<b>Top Talants botiga xush kelibsiz</b>", reply_markup=menuuz)

    except:
        await message.answer("Bot ishlashi uchun <b>➕ Ro'yxatdan o'tish ➕</b> tugmasini bosin", reply_markup=royxat)

@dp.message_handler(content_types=['contact'])
async def phone_number(message: types.Message):
    nick_name = message.contact.full_name
    id = message.contact.user_id
    phone_usm = message.contact.phone_number
    try:
        db.royxat_qoshish(id=id,
            number=phone_usm, nick_name=nick_name,ball=+1,daraja="Entry")
    except:
        pass

    await message.answer(text="Muvaffaqiyatli ro'yhatdan o'tdingiz",reply_markup=menuuz)


# Buyurtmachi ----------------------------------------------------------------------









@dp.message_handler(text="💎 Bal Nima ?")
async def bal(message: types.Message):
    await message.answer(f"Ball bu sizning IT 👨‍💻darajangizni ko'rsatib beruvchi sistema \n\n"
                         f"💻bo'lib sizga admin va buyurtmachilar🪪 tamondan berilgan topshiriqlarni ⌛️baxolab ball beridi.\n"
                         f"Agar siz bironta buyurtmachudan ishni olib topshirsangiz sizga +10 bal beriladi.\n\n"
                         f"<b>Darajalar</b>\n"
                         f"Bu sizni qaysi darajada ekanligingizni belgilaydi. "
                         f"Agar siz Entry levelda bo'lsangiz sizga osonroq buyurtmalar chiqadi."
                         f"Darajangizga qarab buyurtmalar chiqadi.\n"
                         f"\n"
                         f"Agar siz biz bergan topshiriqlarni mukammal topshirsangiz admin tekshirib ma'qul deb topsa darajangiz oshadi🎓", reply_markup=menuuz)