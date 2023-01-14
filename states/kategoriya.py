from aiogram.dispatcher.filters.state import StatesGroup, State

class kategoriya (StatesGroup):
    ismi = State()

class number(StatesGroup):
    number = State()

class Name(StatesGroup):
    name = State()