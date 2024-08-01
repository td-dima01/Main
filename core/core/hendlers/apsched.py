from aiogram import Bot

async def send_message_time(bot: Bot):
    await bot.send_message(5598652988, f'Это сообщение отправится через несколько секунд')

async def send_massage_cron(bot: Bot):
    await bot.send_message(5598652988, f'Это сообщение отправляется каждый день')