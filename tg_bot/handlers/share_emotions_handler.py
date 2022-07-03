from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from tg_bot.keyboards.default.share_emotions_menu import menu
from tg_bot.keyboards.default.general_menu import yes_no_menu, yes_no_dot_menu

from tg_bot.filters.share_emotions import ShareEmotions
from tg_bot.filters.Form import Form

from tg_bot.services import sqlite_db


async def share_emotions_start(message: types.Message):
    await message.answer("Що сталося? Ти можеш розказати мені все! І не хвилюйся: наша розмова конфеденційна",
                         reply_markup=menu)
    await ShareEmotions.level_1.set()


async def call_to_do(message: types.Message, state: FSMContext):
    await message.answer(f"Зверни увагу на твоїх друзів - емоції. Як ти себе почуваєш? Чому ти так себе почуваєш", reply_markup=ReplyKeyboardRemove())
    await ShareEmotions.level_2.set()


async def process_text_or_voice(message: types.Message, state: FSMContext):
    if message.text in ("Так.",):
        await message.answer("Кожного разу, як ти висловлюєшся, всередині стає спокійніше~")
        return
    elif message.text in ("Ні.",):
        user_name = await sqlite_db.get_user_name(message.from_user.id)
        user_name = user_name[0]
        async with state.proxy() as st:
            st["user"] = user_name
        await message.answer(f"Друже {user_name}, а чого б ти хотів зараз?")
        await ShareEmotions.level_3.set()
    else:
        await message.answer(f"Хочеш сказати щось ще?", reply_markup=yes_no_dot_menu)

async def mo_motivate(message: types.Message, state: FSMContext):
    async with state.proxy() as st:
        user_name = st["user"]
    await message.answer(f"Друже {user_name}, якщо ця дія/слова/переживання не заходять на кордони іншої людини і є екологічними - ти маєш зробити щось, щоб отримати те, що ти хочеш!"
                         "\n\nЯ вірю в тебe! "
                         "\n\nАле пам'ятай - ти не маєш нашкодити собі і іншим!", reply_markup=ReplyKeyboardRemove())
    await message.answer(f"Чи бажаєш ти продовжити наше спілкування?", reply_markup=yes_no_menu)
    if await state.get_state():
        await state.finish()
    await Form.general.set()

def register_share_emotions(dp: Dispatcher):
    dp.register_message_handler(share_emotions_start, text="Відкрити своє серце")
    dp.register_message_handler(call_to_do, state=ShareEmotions.level_1)
    dp.register_message_handler(process_text_or_voice, state=ShareEmotions.level_2, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(mo_motivate, state=ShareEmotions.level_3)

