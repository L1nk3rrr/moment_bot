from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from tg_bot.keyboards.default.general_menu import menu


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.reply("Наразі наше спілкування у стані 'невідомого моменту', "
                            "можеш обрати ф-ію яка тобі зараз потрібна з меню", reply_markup=menu)
        return
    await state.finish()
    await message.answer("Добре, відміна~\nМожеш просто завершити наше спілкування, або ж обрати знову один із пунктів~", reply_markup=menu)


def register_general(dp: Dispatcher):
    dp.register_message_handler(cancel_handler, state="*", commands="Відміна")
    dp.register_message_handler(cancel_handler, Text(equals="Відміна", ignore_case=True), state="*")
