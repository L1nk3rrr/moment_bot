from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Написати листа Мо"),
            KeyboardButton(text="Записати щире голосове повідомлення")
        ],
    ],
    resize_keyboard=True,
)

thanks = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Дякую, Мо!"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)