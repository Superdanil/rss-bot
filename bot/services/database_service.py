import http

import aiohttp

from exceptions import DatabaseError
from settings import settings


async def register_user(telegram_id: int) -> None:
    """Добавляет запись пользователя в БД."""
    try:
        async with aiohttp.ClientSession() as session:
            response = await session.post(url=f"{settings.database_url}/users", json={"telegram_id": telegram_id})
        if response.status not in {200, 201}:
            raise DatabaseError from None
    except Exception:
        raise DatabaseError from None


async def add_source(telegram_id: int, message: str) -> bool:
    """Добавляет запись источника новостей в БД."""
    async with aiohttp.ClientSession() as session:
        source = await session.post(
            url=f"{settings.database_url}/sources",
            json={"telegram_id": telegram_id, "source": message},
        )
        if source.status in {200, 201}:
            return True


async def get_news(telegram_id: int, hours: int) -> list | None:
    """Получает новости из БД."""
    async with aiohttp.ClientSession() as session:
        response = await session.get(
            url=f"{settings.database_url}/news",
            params={"telegram_id": telegram_id, "hours": hours},
        )
        if response.status != http.HTTPStatus.OK:
            return None
        newsfeed = await response.json()
        if not newsfeed:
            return []
    return newsfeed
