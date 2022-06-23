from aiogram.dispatcher.filters.state import StatesGroup, State


class ShareEmotions(StatesGroup):
    level_1 = State()
    level_2 = State()
    level_3 = State()

