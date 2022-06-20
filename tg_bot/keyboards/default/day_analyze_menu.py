from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Написати текстово"),
            KeyboardButton(text="Записати голосове повідомлення")
        ],
    ],
    resize_keyboard=True,
)

example = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Приклад"),
        ],
    ],
    resize_keyboard=True,
)

circle = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отримати коло емоцій"),
        ],
    ],
    resize_keyboard=True,
)