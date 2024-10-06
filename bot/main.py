import asyncio
import logging

from aiogram import Bot, Dispatcher

from routers import unknown_command_router
from routers.callbacks import router as callback_router
from routers.commands import support_router, news_router
from settings import settings


async def main():
    dp = Dispatcher()
    dp.include_routers(callback_router, support_router, news_router, unknown_command_router)
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
