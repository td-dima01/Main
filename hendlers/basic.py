from aiogram import Bot
from aiogram.types import Message
from datetime import datetime
import os
from core.keyboards.reply import local_tel_poll
from core.keyboards.inline import selec_macbook

# функция inline кнопок
async def get_inline(message: Message, bot: Bot):
    await message.answer(f'Hello {message.from_user.first_name}. Show inline button',
                         reply_markup=selec_macbook)

async def get_start(message: Message, bot: Bot):
    # Обработчик команды start
    await bot.send_message(message.from_user.id, "Hello")
    await message.answer("Hello gay")
    await message.reply("hello men")

async def help(message: Message, bot: Bot):
    # Обработчик команды help
    await message.answer("Выберите действие:", reply_markup=local_tel_poll)

async def get_location(message: Message, bot: Bot):
    # Обработчик получения геолокации
    await message.answer(f'Спасибо за отправку локации!\n'
                         f'Широта: {message.location.latitude}\n'
                         f'Долгота: {message.location.longitude}')

async def get_contact(message: Message, bot: Bot):
    # Обработчик получения контактных данных
    await message.answer(f'Спасибо за отправку контакта!\n'
                         f'Имя: {message.contact.first_name}\n'
                         f'Фамилия: {message.contact.last_name}\n'
                         f'Номер телефона: {message.contact.phone_number}')

async def get_photo(message: Message, bot: Bot):
    # Обработчик получения фотографии
    if not os.path.exists("./media"):
        os.makedirs("./media")

    await message.answer(f'Отлично, ты отправил фото. Я его сохраню')

    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)

    # Генерация уникального имени файла с использованием временной метки
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    file_path = f'./media/photo_{timestamp}.jpg'

    # Сохранение фото
    await bot.download_file(file.file_path, file_path)