from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboards = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Ряд 1. Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 1. Кнопка 2'
        ),
        KeyboardButton(
            text='Ряд 1. Кнопка 3'
        )
    ],
    [
        KeyboardButton(
            text='Ряд 2. Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 2. Кнопка 2'
        ),
        KeyboardButton(
            text='Ряд 2. Кнопка 3'
        )
    ]
])