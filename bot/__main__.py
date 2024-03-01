import asyncio
import logging

from aiogram import Bot, Dispatcher

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config_reader import config
# from handlers import commands, inline_mode
from handlers import commands
from ui_commands import set_bot_commands


async def main():
    # Задаем логгирование
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # Подключение к БД
    engine = create_async_engine(url=str(config.db_url), echo=False)
    session_maker = async_sessionmaker(engine, expire_on_commit=False)

    # Авторизуем бота
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")

    dp = Dispatcher()

    # Подключаем хендлеры
    dp.include_router(commands.router)
    # dp.include_router(inline_mode.router)

    # Устанавливаем команды бота
    await set_bot_commands(bot)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
