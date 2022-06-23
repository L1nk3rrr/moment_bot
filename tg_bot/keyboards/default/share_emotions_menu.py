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

yes_no_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Так"),
            KeyboardButton(text="Ні")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
