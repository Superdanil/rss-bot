import asyncio
import logging

from aiogram import Bot, Dispatcher

from core.settings import settings
from handlers.users import router as user_router
from handlers.support import router as support_router
from handlers.news import router as news_router


async def main():
    dp = Dispatcher()
    dp.include_routers(support_router, user_router, news_router)
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
