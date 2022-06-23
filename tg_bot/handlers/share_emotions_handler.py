from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from tg_bot.keyboards.default.share_emotions_menu import menu, yes_no_menu

from tg_bot.filters.share_emotions import ShareEmotions


async def share_emotions_start(message: types.Message):
    await message.answer("Що сталося? Ти можеш розказати мені все! І не хвилюйся: наша розмова конфеденційна",
                         reply_markup=menu)
    await ShareEmotions.level_1.set()


async def call_to_do(message: types.Message, state: FSMContext):
    await message.answer(f"Зверни увагу на твоїх друзів - емоції. Як ти себе почуваєш? Чому ти так себе почуваєш", reply_markup=ReplyKeyboardRemove())
    await ShareEmotions.level_2.set()


async def process_text_or_voice(message: types.Message, state: FSMContext):
    if message.text in ("Так",):
        await message.answer("Кожного разу, як ти висловлюєся, всередині стає спокійніше~")
        return
    elif message.text in ("Ні",):
        await message.answer("Друже, а чого б ти хотів зараз?")
        await ShareEmotions.level_3.set()
    else:
        await message.answer(f"Хочеш сказати щось ще?", reply_markup=yes_no_menu)

async def mo_motivate(message: types.Message, state: FSMContext):
    await message.answer("Друже (імя), якщо ця дія/слова/переживання не заходять на кордони іншої людини і є екологічними - ти маєш зробити щось, щоб отримати те, що ти хочеш!"
                         "\n\nЯ вірю в тебe! "
                         "\n\nАле пам'ятай - ти не маєш нашкодити собі і іншим!")
    if await state.get_state():
        await state.finish()

def register_share_emotions(dp: Dispatcher):
    dp.register_message_handler(share_emotions_start, text="Відкрити своє серце")
    dp.register_message_handler(call_to_do, state=ShareEmotions.level_1)
    dp.register_message_handler(process_text_or_voice, state=ShareEmotions.level_2, content_types=types.ContentTypes.ANY)
    dp.register_message_handler(mo_motivate, state=ShareEmotions.level_3)

