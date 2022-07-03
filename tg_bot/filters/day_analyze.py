from aiogram.dispatcher.filters.state import StatesGroup, State


class DayAnalyze(StatesGroup):
    remember = State()
    circle = State()
    states_start = State()
    inside_state = State()
    wants = State()
    last_question = State()
    finish = State()
