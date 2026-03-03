import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from bot.handlers import get_routers


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


def get_bot_token() -> str:
    load_dotenv()
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("Environment variable BOT_TOKEN is not set.")
    return token


async def main() -> None:
    setup_logging()
    bot = Bot(token=get_bot_token())
    dp = Dispatcher()

    for router in get_routers():
        dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Досрочный выход.")
