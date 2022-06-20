from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from tg_bot.filters.Form import Form
from tg_bot.keyboards.default.share_emotions_menu import menu

from tg_bot.filters.share_emotions import ShareEmotions


async def share_emotions_start(message: types.Message):
    await message.answer("Розкажи, що сталося? Що ти відчуваєш? Що хочеш тут і зараз?", reply_markup=menu)
    await ShareEmotions.level_1.set()


async def call_to_do(message: types.Message, state: FSMContext):
    await message.answer(f"Можеш висловлювати все що забажаєш, адже цей чат є повністю приватним~", reply_markup=ReplyKeyboardRemove())
    await ShareEmotions.level_2.set()


async def process_text_or_voice(message: types.Message, state: FSMContext):
    if message.text in ("Написати текстово", "Записати голосове повідомлення"):
        await message.answer("Кожного разу, як ти висловлюєся, всередині стає спокійніше~")
        return
    await message.answer(f"Ти молодчинка!")
    await message.answer(f"Якщо бажаєш ще щось висловити, можеш обрати пунктик з меню~", reply_markup=menu)


def register_share_emotions(dp: Dispatcher):
    dp.register_message_handler(share_emotions_start, text="Поділитись емоціями")

    dp.register_message_handler(call_to_do, state=ShareEmotions.level_1)
    dp.register_message_handler(process_text_or_voice, state=ShareEmotions.level_2, content_types=types.ContentTypes.ANY)

