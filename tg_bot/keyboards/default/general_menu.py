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

yes_no_dot_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Так."),
            KeyboardButton(text="Ні.")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

too_thx = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Це взаємно, Мо!"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
