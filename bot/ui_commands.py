from aiogram import Bot
from aiogram.types import BotCommand


async def set_bot_commands(bot: Bot) -> None:
    """
    Set bot commands in UI (using Menu or "/" buttons)
    :param bot: Bot object
    """
    commands = [
        BotCommand(command="start", description="Старт"),
        BotCommand(command="shop", description="Магазин"),
        BotCommand(command="manager", description="Менеджер"),
        BotCommand(command="help", description="О боте")
    ]

    await bot.set_my_commands(commands=commands)
