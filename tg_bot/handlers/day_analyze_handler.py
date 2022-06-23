import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from tg_bot.filters.Form import Form
from tg_bot.keyboards.default.day_analyze_menu import menu, example, circle

from tg_bot.filters.day_analyze import DayAnalyze
from images.images_setup import IMAGE_DIR, os


async def day_analyze_start(message: types.Message):
    await message.answer(
        "Друже, згадай найяскравіші ситуації протягом дня та розкажи мені свої стани та емоції, з яких складалися стани.\n "
        "Можеш прописати, або ж натиснути на \"Приклад\" для отримання прикладу",
        reply_markup=example)
    await DayAnalyze.remember.set()


async def examples_and_transaction(message: types.Message, state: FSMContext):
    if message.text == "Приклад":
        await message.answer("Наприклад."
                             "\nКоли я гуляв сьогодні центром міста я відчував паніку."
                             "\nХмм. З яких емоцій складається Паніка?")
        await asyncio.sleep(2)

        await message.answer("Тоді паніка складалася з страху, злості, образи, самотності")
        await asyncio.sleep(1)

        await message.answer("Коли ти зрозумієш свої емоції не забудь відповісти на питання \"Звідки вони? або чому?\"")
        await asyncio.sleep(2)

        await message.answer("Наприклад:\n"
                       "Страх - Чого я боюся?\n"
                       "Злість - На що, на кого?\n"
                       "Образа - На кого, за що?\n"
                       "Самотність - Хто потрібний?\n"
                       "Марність - Чого я не можу\n")

    await message.answer("Якось так.. Для кращого розумння покажу тобі коло емоцій", reply_markup=circle)
    await DayAnalyze.circle.set()


async def send_circle_start(message: types.Message, state: FSMContext):
    async with open(os.path.join(IMAGE_DIR, "emotion_analyze.png"), "rb") as img:
        await message.answer_photo(img)
    await message.answer("Це коло емоцій. Воно допоможе тобі краще зрозуміти які емоції ти відчував/ла в різних ситуаціях і станах")


def register_day_analyze(dp: Dispatcher):
    dp.register_message_handler(day_analyze_start, text="Розказати про мій день")

    dp.register_message_handler(examples_and_transaction, state=DayAnalyze.remember)
    dp.register_message_handler(send_circle_start, state=DayAnalyze.circle)

