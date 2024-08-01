from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

# Пример клавиатуры с множеством кнопок
reply_keyboards = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Ряд 1. Кнопка 1'),
        KeyboardButton(text='Ряд 1. Кнопка 2'),
        KeyboardButton(text='Ряд 1. Кнопка 3')
    ],
    [
        KeyboardButton(text='Ряд 2. Кнопка 1'),
        KeyboardButton(text='Ряд 2. Кнопка 2'),
        KeyboardButton(text='Ряд 2. Кнопка 3')
    ]
], resize_keyboard=True, one_time_keyboard=True,
input_field_placeholder='Выберите кнопку ->', selective=True)

# Клавиатура для отправки геолокации, контакта и создания викторины
local_tel_poll = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Отправить геолокацию", request_location=True),
        KeyboardButton(text="Отправить контакт", request_contact=True)
    ],
    [
        KeyboardButton(text="Создать викторину", request_poll=KeyboardButtonPollType(type="regular"))
    ]
], resize_keyboard=True, one_time_keyboard=False,
input_field_placeholder='Выберите действие')