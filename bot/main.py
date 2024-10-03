import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.routers.callback_handlers import router as callback_router
from bot.routers.commands import users_router, support_router, news_router
from core.settings import settings


async def main():
    dp = Dispatcher()
    dp.include_routers(callback_router, support_router, users_router, news_router)
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
