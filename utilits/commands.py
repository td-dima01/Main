from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def get_commands(bot: Bot):
    # Определение команд бота
    commands = [
        BotCommand(command="start", description="Начало работы"),
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="cancel", description="Сбросить"),
        BotCommand(command="inline", description="Show inline keyboard")
    ]
    # Установка команд для бота
    await bot.set_my_commands(commands, BotCommandScopeDefault())