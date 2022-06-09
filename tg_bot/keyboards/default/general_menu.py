from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Поділитись емоціями")
        ],
        [
            KeyboardButton(text="Аналіз дня")
        ]
    ],
    resize_keyboard=True
)
