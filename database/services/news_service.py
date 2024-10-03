from database.core.dtos import NewsCreateDTO, NewsReadDTO
from database.repositories import IDBHelper
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
        # dto.url = "https://dostup1.ru/rss/"

        async with self._db_helper.session_getter() as session:
            news_list = await self._repository.bulk_create(dto_list, session)
            await self._db_helper.commit(session)
            return news_list

    async def get_users_news(self, telegram_id: int, timedelta: int):
        async with self._db_helper.session_getter() as session:
            news = await self._source_repository.get_by_user(telegram_id, timedelta, session)
