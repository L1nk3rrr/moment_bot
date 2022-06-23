from create_bot import bot
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.webhook import SendMessage
from aiogram.types import ReplyKeyboardRemove

from tg_bot.keyboards.default.general_menu import menu

from tg_bot.filters.Form import Form


async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Привіт! Мене звати Мо і я буду допомагати тобі з твоїми емоційми і розумінням себе",
                         reply_markup=ReplyKeyboardRemove())
    await Form.general.set()
    await message.answer("Як до тебе звертатись?")


async def general_menu(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    if message.text != "Ні":
        await bot.send_message(user_id, "Як тобі допомогти?", reply_markup=menu)
    else:
        await bot.send_message(user_id, "Дякую, що написав_ла.\nНадіюсь тобі стало трішки ліпше, адже це моя місія!\n"
                             "Можеш звертатись до мене у будь-який час~~~")
    if await state.get_state():
        await state.finish()


def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, Command("start"), state="*")
    dp.register_message_handler(general_menu, state=Form.general)
