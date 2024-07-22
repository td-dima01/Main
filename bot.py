from aiogram import Bot, Dispatcher
from aiogram.types import ContentType, Message #ContenType
from core.hendlers.basic import get_start, get_photo, help
import asyncio
import logging
from aiogram.filters import Command
from core.utilits.commands import get_commands
#from aiogram.filters import ContentTypesFilter
from aiogram import F

with open('toc.txt', 'r') as file:
    token = file.read().strip()

async def start_bot(bot: Bot):
    await bot.send_message(5598652988, text="bot run")
    await get_commands(bot)
async def stop_bot(bot: Bot):
    await bot.send_message(5598652988, text="bot stop")

async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=token)

    dp = Dispatcher()
    dp.message.register(get_start, Command(commands=["start","run"]))
    dp.message.register(help, Command(commands=["help","помощь"]))
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    #dp.message.register(get_photo, F.content_types == ContentType.PHOTO)
    dp.message.register(get_photo, F.photo)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
