from create_bot import bot
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.emoji import emojize

from tg_bot.keyboards.default.general_menu import menu, too_thx, go_mo

from tg_bot.filters.Form import Form
from tg_bot.filters.admin import AdminFilter
from tg_bot.filters.auth import Register
from tg_bot.services import sqlite_db


async def bot_start(message: types.Message, state: FSMContext):
    user_name = await sqlite_db.get_user_name(message.from_user.id)
    await message.answer("Привіт! Мене звати Мо.\n"
                         "Я буду допомагати тобі з твоїми емоціями і розумінням себе" + emojize(":cherry_blossom:"),
                         reply_markup=go_mo)
    if not user_name:
        await Form.general.set()
        async with state.proxy() as st:
            st["auth"] = True
        await message.answer("Як до тебе звертатись?")
    else:
        await Form.general.set()


async def general_menu(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as st:
        if st.get("auth"):
            st["auth"] = False
            await sqlite_db.new_user(message.from_user.id, message.text)
    if message.text != "Ні":
        await bot.send_message(user_id, "Як тобі допомогти?", reply_markup=menu)
    else:
        await bot.send_message(user_id, emojize("Дякую, що написав_ла:heartpulse:\n"
                                        "Надіюсь тобі стало трішки ліпше, адже це моя місія!\n"
                                        "Можеш звертатись до мене у будь-який час~~~:smiling_face_with_hearts:"),
                               reply_markup=ReplyKeyboardRemove())
    if await state.get_state():
        await state.finish()

async def filter_bad(message: types.Message):
    await message.reply("Непотрібно так, це перейшло певні межі.")
    await message.delete()

def register_start(dp: Dispatcher):
    dp.register_message_handler(filter_bad, AdminFilter(), state="*")
    dp.register_message_handler(bot_start, Command("start"), state="*")
    dp.register_message_handler(general_menu, state=Form.general)
