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
