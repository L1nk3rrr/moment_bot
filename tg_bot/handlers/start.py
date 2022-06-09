from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.webhook import SendMessage
from aiogram.types import ReplyKeyboardRemove

from tg_bot.keyboards.default.general_menu import menu

from tg_bot.filters.Form import Form


async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Привіт, я бот Moment!\n"
                         "Хочу допомогти тобі з твоїми емоціями і стресом.\n", reply_markup=ReplyKeyboardRemove())
    await Form.register.set()
    await message.answer("Перед початком, вкажи будь ласка як до тебе звертатись.")


async def hello_user(message: types.Message, state: FSMContext):
    await message.answer(f"Приємно познайомитись, {message.text}!\n"
                         "Готова_ий розпочати?")
    await Form.general.set()


async def general_menu(message: types.Message, state: FSMContext):
    if message.text != "Ні":
        await message.answer("Як тобі допомогти?", reply_markup=menu)
    else:
        await message.answer("Дякую, що написав_ла.\nНадіюсь тобі стало трішки ліпше, адже це моя місія!.\n"
                             "Можеш звертатись до мене у будь-який час~~~")
    if await state.get_state():
        await state.finish()


def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, Command("start"))
    dp.register_message_handler(hello_user, state=Form.register)
    dp.register_message_handler(general_menu, state=Form.general)
    dp.register_message_handler(general_menu, state=Form.general)
