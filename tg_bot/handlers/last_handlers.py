import json
import string

from aiogram import types, Dispatcher


async def bot_unknown_answer(message: types.Message):
    await message.answer("Вибач, але я покищо не знаю такої команди..\nВибери зі списки, або ж розпочним спочатку /start")

def register_last(dp: Dispatcher):
    dp.register_message_handler(bot_unknown_answer, state="*", content_types=types.ContentTypes.ANY)