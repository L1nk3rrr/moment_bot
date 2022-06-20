from aiogram.dispatcher.filters.state import StatesGroup, State


class DayAnalyze(StatesGroup):
    remember = State()
    circle = State()
