from aiogram import Bot
from aiogram.types import Message
from datetime import datetime
import os
import json
from core.keyboards.reply import reply_keyboards

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, "Hello")
    await message.answer("Hello gay",) # не нужно прописывать чат id
    await message.reply("hello men") # цытирование ботом

async def help(message: Message, bot: Bot):
    await message.answer("Выбери что нужно", reply_markup=reply_keyboards)

async def get_photo(message: Message, bot: Bot):
    if not os.path.exists("./media"):
        os.makedirs("./media")

    await message.answer(f'Отлично, ты отправил фото.Я его сохраню')

    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    file_path = f'./media/photo_{timestamp}.jpg'

    await bot.download_file(file.file_path, file_path)


# async def get_photo(message: Message, bot: Bot):
#     await message.answer(f'Отлично, ты отправил фото.Я его сохраню')
#     file = await bot.get_file(message.photo[-1].file_id)
#     await bot.download_file(file.file_path, './media/photo.jpg')
