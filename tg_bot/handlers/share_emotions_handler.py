import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.emoji import emojize

from tg_bot.keyboards.default.share_emotions_menu import menu
from tg_bot.keyboards.default.general_menu import yes_no_menu, yes_no_dot_menu

from tg_bot.filters.share_emotions import ShareEmotions
from tg_bot.filters.Form import Form

from tg_bot.services import sqlite_db


async def share_emotions_start(message: types.Message):
    await message.answer("Що сталося?\n\n"
                         "*Ти можеш розказати мені все!\n"
                         "Не хвилюйся: наша розмова конфіденційна",
                         reply_markup=menu)
    await ShareEmotions.level_1.set()


async def call_to_do(message: types.Message, state: FSMContext):
    await message.answer("Зверни увагу на свої емоції.\n"
                         "Вони твої друзі!\n", reply_markup=ReplyKeyboardRemove())

    await asyncio.sleep(3)

    await message.answer("Як ти себе почуваєш?\n"
                         "Чому ти так себе почуваєш?\n")
    await ShareEmotions.level_2.set()


async def process_text_or_voice(message: types.Message, state: FSMContext):
    if message.text in ("Так.",):
        await message.answer("Кожного разу, як ти висловлюєшся, всередині стає спокійніше~" + emojize(":relaxed:"),
                             reply_markup=ReplyKeyboardRemove())
        return
    elif message.text in ("Ні.",):
        user_name = await sqlite_db.get_user_name(message.from_user.id)
        user_name = user_name[0]
        async with state.proxy() as st:
            st["user"] = user_name
        await message.answer(f"Друже {user_name}, а чого б ти хотів/ла зараз?", reply_markup=ReplyKeyboardRemove())
        await ShareEmotions.level_3.set()
    else:
        await message.answer(f"Хочеш сказати щось ще?", reply_markup=yes_no_dot_menu)


async def mo_motivate(message: types.Message, state: FSMContext):
    async with state.proxy() as st:
        user_name = st["user"]
    await asyncio.sleep(2)
    await message.answer(f"Друже {user_name}, якщо ця дія/слова/переживання не перетинають кордони іншої людини і є "
                         "екологічними - ти маєш зробити щось, щоб отримати те, що ти хочеш!" + emojize(":heart::pray:"),
                         reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(4)
    await message.answer("Я вірю в тебe!")
    await asyncio.sleep(2)
    await message.answer("Але пам'ятай - ти не маєш нашкодити собі і іншим!")
    await asyncio.sleep(3)
    await message.answer(f"Чи бажаєш продовжити наше спілкування?", reply_markup=yes_no_menu)
    if await state.get_state():
        await state.finish()
    await Form.general.set()

def register_share_emotions(dp: Dispatcher):
    dp.register_message_handler(share_emotions_start, text="Відкрити своє серце")
    dp.register_message_handler(call_to_do, state=ShareEmotions.level_1)
    dp.register_message_handler(process_text_or_voice, state=ShareEmotions.level_2, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(mo_motivate, state=ShareEmotions.level_3)

