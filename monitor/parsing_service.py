import asyncio
import datetime
import time

import aiohttp
import feedparser
from loguru import logger

from database_service import database_service
from dtos import SourceDTO, NewsDTO


async def parse_rss() -> None:
    rss_sources: list[SourceDTO] = database_service.get_rss_sources()
    logger.debug(f"Получен список источников длиной {len(rss_sources)}.")
    if not rss_sources:
        return None
    news_list = []

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_rss(session, source.url) for source in rss_sources]
        results = await asyncio.gather(*tasks)

        one_minute_ago = datetime.datetime.now(datetime.UTC) - datetime.timedelta(minutes=600)

        for source, parsed_source in zip(rss_sources, results):
            if parsed_source is None:
                continue

            for entry in parsed_source.entries:
                published_time = None
                if hasattr(entry, 'published_parsed'):
                    published_time = datetime.datetime.fromtimestamp(time.mktime(entry.published_parsed), datetime.UTC)

                if published_time and published_time > one_minute_ago:
                    news_item = NewsDTO(
                        title=entry.title,
                        link=entry.link,
                        published_at=published_time,
                        source_id=source.id,
                    )
                    news_list.append(news_item)
    if news_list:
        logger.debug(f"Получено {len(news_list)} новостей для добавления в базу данных.")
        database_service.add_news(news_list)


async def fetch_rss(session, source_url: str):
    try:
        async with session.get(source_url) as response:
            content = await response.text()
            parsed_source = feedparser.parse(content)
            if parsed_source.bozo:
                return None
            return parsed_source
    except Exception as e:
        logger.error(f"При попытке распарсить RSS возникло исключение: {e}")
        return None
