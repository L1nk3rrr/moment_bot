from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text

from tg_bot.filters.Form import Form
from tg_bot.keyboards.default.analyze_menu import menu, exit, yes_no

from tg_bot.filters.day_analyze import DayAnalyze


async def analyze_start(message: types.Message):
    await message.answer("Розкажи, що сталося? Що ти відчуваєш? Що хочеш тут і зараз?", reply_markup=menu)
    await DayAnalyze.level_1.set()


async def cancel_handler(message: types.Message, state: FSMContext):
    """Allow user to cancel action via /cancel command"""

    current_state = await state.get_state()
    if current_state is None:
        # User is not in any state, ignoring
        return
    await state.finish()
    await Form.general.set()
    await message.answer("Продовжуємо?", reply_markup=yes_no)

async def call_to_do(message: types.Message, state: FSMContext):
    await message.answer(f"Можеш висловлювати все що забажаєш, адже цей чат є повністю приватним~", reply_markup=exit)
    await DayAnalyze.level_2.set()

async def process_text_or_voice(message: types.Message, state: FSMContext):
    await message.answer(f"Ти молодець, що зміг_ла поділитись цим, можливо ще щось?\n"
                        "Якщо ж ні, просто натисни \"Назад\" або /cancel.")



def register_day_analyze(dp: Dispatcher):
    dp.register_message_handler(analyze_start, text="Аналіз дня")
    dp.register_message_handler(cancel_handler, state="*", commands=["cancel"])
    dp.register_message_handler(cancel_handler, state="*", text="Назад")
    dp.register_message_handler(call_to_do, state=DayAnalyze.level_1)
    dp.register_message_handler(process_text_or_voice, state=DayAnalyze.level_2)
