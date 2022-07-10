import asyncio

from aiogram import types, Dispatcher
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from tg_bot.filters.Form import Form
from tg_bot.keyboards.default.day_analyze_menu import example, circle
from tg_bot.keyboards.default.general_menu import yes_no_menu

from tg_bot.filters.day_analyze import DayAnalyze
from tg_bot.services import sqlite_db


async def day_analyze_start(message: types.Message):
    user_name = await sqlite_db.get_user_name(message.from_user.id)
    user_name = user_name[0]
    await message.answer(f"{user_name}, згадай найяскравіші ситуації протягом дня.", reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(2)
    await message.answer("Розкажи мені про свої стани та емоції в тій чи іншій ситуації.")
    await asyncio.sleep(2)
    await message.answer(emojize("Не розумієш?:thinking_face:\n" 
                         "Тисни «Приклад» і я поясню."), reply_markup=example)
    await DayAnalyze.remember.set()


async def examples_and_transaction(message: types.Message, state: FSMContext):
    if message.text == "Приклад":
        await message.answer("Наприклад:\n"
                             "Коли я гуляв сьогодні центром міста я відчував паніку.\n"
                             "Паніка – це стан\n\n"
                             "Хмм, а з яких емоцій складається паніка?", reply_markup=ReplyKeyboardRemove())
        await asyncio.sleep(5)

        await message.answer("Точно!" + emojize(":nerd_face:") +
                             "\nПаніка в тій ситуації складалася з страху, злості, образи, самотності.\n\n"
                             "Страх, злість, образа, самотність - це емоції")
        await asyncio.sleep(5)

        await message.answer(emojize("Коли ти зрозумієш свої емоції не забудь відповісти на питання:\n"
                             ":small_blue_diamond:\"Звідки ці емоції? Чому я їх переживаю?\""))
        await asyncio.sleep(4)

        await message.answer("Наприклад в моєму випадку з прогулянкою:\n\n"
                             "Страх - Чого я боюся?\n"
                             "Злість - На що, на кого?\n"
                             "Образа - На кого, за що?\n"
                             "Самотність - Хто мені потрібний?\n"
                             "Марність - Чого я не можу\n"
                             "і т.д.")
        await asyncio.sleep(7)

    await message.answer("А якими ще емоціями можна описати стани?" + emojize(":thinking_face:"), reply_markup=circle)
    await DayAnalyze.circle.set()


async def send_circle_start(message: types.Message, state: FSMContext):
    with open("./images/emotion_analyze.png", "rb") as img:
        await message.answer_photo(img)
    await message.answer("Це коло емоцій. Воно допоможе тобі краще зрозуміти які емоції ти відчував/ла в різних ситуаціях і станах", reply_markup=ReplyKeyboardRemove())
    await message.answer("То можемо розпочинати?" + emojize(":face_savoring_food:"), reply_markup=yes_no_menu)
    await DayAnalyze.states_start.set()


async def states_start(message: types.Message, state: FSMContext):
    await message.answer(emojize(":small_blue_diamond:Які ти згадуєш найяскравіші ситуації за день?\n"
                         ":small_blue_diamond:В яких станах та перебував/ла?\n"
                         ":small_blue_diamond:З яких емоцій,як конструктор, складався твій стан?"), reply_markup=ReplyKeyboardRemove())
    await DayAnalyze.inside_state.set()


async def inside_state(message: types.Message, state: FSMContext):
    await message.answer("Якщо зануритись в ті стани та ситуації, то чого ти тоді хотів/ла?")
    await DayAnalyze.wants.set()


async def wants(message: types.Message, state: FSMContext):
    await message.answer("А чого не хотів/ла?")
    await DayAnalyze.last_question.set()


async def last_question(message: types.Message, state: FSMContext):
    await message.answer("І останнє питання:\n\n"
                         "А які емоції ти хотів/ла переживати тоді?\n\n"
                         "І що ти робиш для того, щоб бути в цих емоція і отримати те, що ти хочеш?\n"
                         "Або що треба зробити для цього?")
    await DayAnalyze.finish.set()


async def finish(message: types.Message, state: FSMContext):
    user_name = await sqlite_db.get_user_name(message.from_user.id)
    user_name = user_name[0]
    await message.answer(f"Друже,{user_name}, ти величезний молодець!")
    await asyncio.sleep(2)

    await message.answer("Дякую, що поділився/лась зі мною своїми переживаннями" + emojize(":cupid:"))
    await asyncio.sleep(2)

    await message.answer(emojize("Поговоримо про важливе..:disguised_face:\n\n"
                         "Обережно нагадаю тобі, що якщо дія/слова/переживання не перетинають "
                         "кордони іншої людини і є екологічними - ти обов'язково маєш зробити щось, щоб отримати те, "
                         "що ти хочеш!:heart::pray:\n\n"
                         "Я вірю в тебе!\n\n"
                         "Але пам'ятай - ти не маєш нашкодити собі й іншим!"))
    await asyncio.sleep(7)

    await message.answer("І ще одне: ти можеш кожного дня розповідати мені про свої стани та емоції, а потім повертатися до цих записів")
    await asyncio.sleep(4)

    await message.answer("Навіщо?" + emojize(":thinking_face:") + "Так ти будеш краще розуміти себе та те, що ти насправді хочеш.\n"
                         "А також відслідковувати свої емоційні стани протягом довгого часу, щоб зрозуміти які емоції ти"
                         " найчастіше переживаєш.")
    await asyncio.sleep(5)
    await message.answer("Може треба щось змінити і відмовитись від якихось трігерів?" + emojize(":astonished_face:"))
    await asyncio.sleep(3)
    await message.answer("Згодом обов'язково розкажи мені про свої спостереження!")
    await asyncio.sleep(3)

    await message.answer("Не губімось! Мо завжди на зв'язку " + emojize(":heart:"))
    await state.finish()
    await Form.general.set()


def register_day_analyze(dp: Dispatcher):
    dp.register_message_handler(day_analyze_start, text="Розказати про мій день")
    dp.register_message_handler(examples_and_transaction, state=DayAnalyze.remember)
    dp.register_message_handler(send_circle_start, state=DayAnalyze.circle)
    dp.register_message_handler(states_start, state=DayAnalyze.states_start)
    dp.register_message_handler(inside_state, state=DayAnalyze.inside_state)
    dp.register_message_handler(wants, state=DayAnalyze.wants)
    dp.register_message_handler(last_question, state=DayAnalyze.last_question)
    dp.register_message_handler(finish, state=DayAnalyze.finish)
