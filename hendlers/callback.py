from aiogram import Bot
from aiogram.types import CallbackQuery

async def select_macbook(call: CallbackQuery, bot: Bot):
    model = call.data.split('_')[1]
    chip = call.data.split('_')[2]
    year = call.data.split('_')[3]

    answer = f'{call.message.from_user.first_name}, ты выбрал Macbook {model}, на чипе {chip}, {year} года'
    await call.message.answer(answer)   
    await call.answer()
