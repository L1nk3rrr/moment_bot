from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


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
            KeyboardButton(text="Отримати коло емоцій на допомогу"),
        ],
    ],
    resize_keyboard=True,
)