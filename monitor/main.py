import asyncio
import time

import schedule

from log_handler import logger
from parsing_service import parse_rss
from settings import settings


def run_async_task():
    logger.debug("Цикл парсинга RSS запущен.")
    asyncio.run(parse_rss())


if __name__ == "__main__":
    logger.info("Монитор запущен.")
    schedule.every(settings.WAITING).minutes.do(run_async_task)
    while True:
        schedule.run_pending()
        time.sleep(1)
