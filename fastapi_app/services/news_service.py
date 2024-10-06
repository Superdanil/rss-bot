from datetime import datetime, timedelta

from pydantic import ValidationError

from core.dtos import NewsCreateDTO, NewsReadDTO
from repositories import IDBHelper
from .service_depends import INewsRepository


class NewsService:
    """Класс работы с новостями."""

    def __init__(
            self,
            repository: INewsRepository,
            db_helper: IDBHelper
    ):
        self._repository = repository
        self._db_helper = db_helper

    async def add_news(self, dto_list: list[NewsCreateDTO]) -> list[NewsReadDTO]:
        """Создаёт запись новости в БД."""
        async with self._db_helper.session_getter() as session:
            news_list = await self._repository.bulk_create(dto_list, session)
            await self._db_helper.commit(session)
            return news_list

    async def get_users_news(self, telegram_id: int, hours: int) -> list[NewsReadDTO]:
        """Возвращает новостную ленту пользователя за timedelta часов."""
        if hours not in (1, 24):
            raise ValidationError("Только за 1 или 24 часа.")
        filter_date = datetime.now() - timedelta(hours=hours)

        async with self._db_helper.session_getter() as session:
            news = await self._repository.get_by_telegram_id(telegram_id, filter_date, session)
        return news
