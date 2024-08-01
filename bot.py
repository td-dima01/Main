from aiogram import Bot, Dispatcher
#from aiogram.types import Message
from core.hendlers.basic import get_start, get_photo, help, get_location, get_contact, get_inline
import asyncio
import logging
from aiogram.filters import Command
from core.utilits.commands import get_commands
from aiogram import F
from core.hendlers.callback import select_macbook
from apscheduler.schedulers.asyncio import AsyncIOScheduler # type: ignore
from core.hendlers import apsched
from datetime import datetime, timedelta


# Чтение токена бота из файла
with open('toc.txt', 'r') as file:
    token = file.read().strip()

async def start_bot(bot: Bot):
    # Отправка сообщения о запуске бота
    await bot.send_message(5598652988, text="bot run")
    await get_commands(bot)

async def stop_bot(bot: Bot):
    # Отправка сообщения об остановке бота
    await bot.send_message(5598652988, text="bot stop")

async def start():
    # Настройка логирования
    logging.basicConfig(level=logging.INFO)
    
    # Инициализация бота и диспетчера
    bot = Bot(token=token)
    dp = Dispatcher()
    

    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(apsched.send_message_time, trigger='date', run_date=datetime.now() + timedelta(seconds=10), 
                      kwargs={'bot': bot})#args=[bot]
    scheduler.add_job(apsched.send_massage_cron, trigger='cron', hour=datetime.now().hour, 
                      minute=datetime.now().minute, second=datetime.now().second + 1,start_date=datetime.now(), kwargs={'bot': bot})
    scheduler.start()


    # Регистрация обработчиков сообщений
    dp.message.register(get_start, Command(commands=["start","run"]))
    dp.message.register(help, Command(commands=["help","помощь"]))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_location, F.location)
    dp.message.register(get_contact, F.contact)
    dp.message.register(get_inline, Command(commands='inline'))
    dp.callback_query.register(select_macbook, F.data.startswith('macbook_'))

    try:
        # Запуск бота
        await dp.start_polling(bot)
    finally:
        # Закрытие сессии бота при завершении работы
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())