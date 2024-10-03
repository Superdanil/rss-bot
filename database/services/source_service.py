import asyncio

import aiohttp
import feedparser
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from database.core.dtos.source_dto import SourceCreateDTO
from database.repositories import IDBHelper
from database.repositories import RepositoryError
from .service_depends import ISourceRepository, IUserSourceAssociationRepository
from ..core.dtos import SourceReadDTO


class SourceService:
    """Класс работы с источниками новостей."""

    def __init__(
            self,
            repository: ISourceRepository,
            user_source_repository: IUserSourceAssociationRepository,
            db_helper: IDBHelper,
    ):
        self._repository = repository
        self._user_source_repository = user_source_repository
        self._db_helper = db_helper

    async def add_or_get_source(self, source: str, session: AsyncSession) -> SourceReadDTO:
        """Создаёт запись источника новостей в БД или возвращает существующий."""
        if not await self._is_rss_source(source):
            raise ValidationError("Енто не RSS!!!")

        existing_source = await self._repository.get_by_url(source, session)
        if existing_source:
            return existing_source

        return await self._repository.add_news(source, session)

    async def get_source_list(self, limit: int, offset: int) -> list[str]:

        async with self._db_helper.session_getter() as session:
            return await self._repository.get_sources(session, limit, offset)

    async def _is_rss_source(self, source: str) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(source, timeout=3) as response:
                    if response.status != 200:
                        return False

                    content_type = response.headers.get('Content-Type', '').lower()
                    if 'xml' in content_type or 'rss' in content_type:
                        return True

                    content = await response.text()
                    feed = feedparser.parse(content)
                    if feed.bozo == 0 and feed.entries:
                        return True

        except (aiohttp.ClientError, asyncio.TimeoutError):
            pass

        return False
