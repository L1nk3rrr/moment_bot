from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from tg_bot.filters.Form import Form
from tg_bot.keyboards.default.day_analyze_menu import menu, example, circle

from tg_bot.filters.day_analyze import DayAnalyze


async def day_analyze_start(message: types.Message):
    await message.answer(
        "Друже, згадай ситуації протягом дня та розпиши свої стани та емоції, з яких складалися стани.\n "
        "Можеш прописати, або ж натиснути на \"Приклад\" для отримання прикладу",
        reply_markup=example)
    await DayAnalyze.remember.set()


async def examples_and_transaction(message: types.Message, state: FSMContext):
    if message.text == "Приклад":
        await message.answer("Я відчуваю паніку.\nПаніку, у свою чергу, може скаладатися з багатьох емоцій")
        await message.answer("Страх - Чого я боюся?\n"
                       "Злість - На що, на кого?\n"
                       "Образа - На кого, за що?\n"
                       "Марність - Чого я не можу\n")

    await message.answer("Якось так.. Для кращого розумння покажу тобі коло емоцій", reply_markup=circle)
    await DayAnalyze.circle.set()


async def send_circle_start(message: types.Message, state: FSMContext):
    await message.answer_photo(open("D:/00Job/asinc_bot_training/tg_bot/images/emotion_analyze.jpg", "rb"))
    await message.answer("Відміна або ж /start")


def register_day_analyze(dp: Dispatcher):
    dp.register_message_handler(day_analyze_start, text="Аналіз дня")

    dp.register_message_handler(examples_and_transaction, state=DayAnalyze.remember)
    dp.register_message_handler(send_circle_start, state=DayAnalyze.circle)

