from aiogram.dispatcher.filters.state import StatesGroup, State

class buyrtma (StatesGroup):
    project_name = State()
    qisqacha_nomi = State()
    project_narxi = State()
    phonenum = State()
    tasdiqlash = State()
    orqaga = State()

class taklif (StatesGroup):
    inline = State()
    taklif=State()
    narxi =State()
    aloqa = State()
    tasdiqlash= State()
    Buyurtmachi = State()

class start (StatesGroup):
    entry = State()
    daraja1 = State()
    daraja2 = State()
    middle = State()
    expert = State()

class topish(StatesGroup):
    buyurtma_topish=State()