import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_reader import config
from handlers import commands


async def main():
    # Задаем логгирование
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # Авторизуем бота
    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")

    dp = Dispatcher()

    # ПОдключение роутеров
    dp.include_router(commands.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
