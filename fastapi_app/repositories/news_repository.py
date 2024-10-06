from datetime import datetime

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert as postgres_insert
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from core.dtos import NewsCreateDTO, NewsReadDTO
from core.models import News, UserSourceAssociation, Source, User
from core.exceptions import RepositoryError
from repositories.base_repository import BaseRepository
from repositories.repository_depends import IDBHelper, ISourceRepository


class NewsRepository(BaseRepository):
    _model = News
    _source_repository = ISourceRepository

    def __init__(self, db_helper: IDBHelper):
        self._db_helper = db_helper

    async def bulk_create(self, dto_list: list[NewsCreateDTO], session: AsyncSession) -> list[NewsReadDTO]:
        """Создаёт записи новостей в БД."""
        news_list = [dto.model_dump() for dto in dto_list]
        stmt = postgres_insert(self._model).values(news_list)
        stmt = stmt.on_conflict_do_nothing().returning(self._model)
        try:
            rows = await session.execute(stmt)
            news_list = rows.scalars()
            return [self._get_dto(news, NewsReadDTO) for news in news_list]

        except SQLAlchemyError as e:
            raise RepositoryError(e) from e

    async def get_by_telegram_id(
        self,
        telegram_id: int,
        filter_date: datetime,
        session: AsyncSession,
    ) -> list[NewsReadDTO]:
        """Возвращает новостную ленту пользователя за timedelta."""
        query = (
            select(self._model)
            .join(Source)
            .join(UserSourceAssociation)
            .join(User)
            .where(User.telegram_id == telegram_id, self._model.published_at >= filter_date)
            .order_by(self._model.published_at.desc())
        )
        try:
            results = await session.execute(query)
            results = results.scalars().all()
            return [self._get_dto(news, NewsReadDTO) for news in results]

        except SQLAlchemyError as e:
            raise RepositoryError(e) from e
