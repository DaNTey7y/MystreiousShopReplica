import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_reader import config


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")

    dp = Dispatcher()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
