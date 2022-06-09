from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Написати текство"),
            KeyboardButton(text="Записати голосове повідомлення")
        ],
        [
            KeyboardButton(text="Назад")
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

exit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад")
        ]
    ]
)

yes_no = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Так"),
            KeyboardButton(text="Ні")
        ]
    ]
)