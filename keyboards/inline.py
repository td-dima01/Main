from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#похоже на reply но немного лучше кнопки
selec_macbook = InlineKeyboardMarkup(inline_keyboard=[
    [
    InlineKeyboardButton(
    text='macbook_13_mi_pro_2020',
    callback_data='macbook_13_pro_2020'
    )
],
[
    InlineKeyboardButton(
        text='macbook_15_mi_2022',
        callback_data='macbook_15_mi_2022'
    )
],
# ссылки на сайт и тг
[
    InlineKeyboardButton(
        text='link',
        url='http://google.com'
    )
],
[
   InlineKeyboardButton(
        text='Profil',
        url='https://t.me/DSP287'
    ) 
]
])
