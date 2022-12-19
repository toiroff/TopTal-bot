from aiogram.dispatcher.filters.state import StatesGroup, State

class buyrtma (StatesGroup):
    project_name = State()
    qisqacha_nomi = State()
    project_narxi = State()
    phonenum = State()
    tasdiqlash = State()
    orqaga = State()

class taklif (StatesGroup):
    taklif=State()
    narxi =State()
    aloqa = State()
    tasdiqlash= State()

class start (StatesGroup):
    entry = State()
    middle = State()
    expert = State()
