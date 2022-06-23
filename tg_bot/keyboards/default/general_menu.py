from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Відкрити своє серце")
        ],
        [
            KeyboardButton(text="Розказати про мій день")
        ]
    ],
    resize_keyboard=True
)
