from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    register = State()
    general = State()
