from typing import Never

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from database.core.dtos import NewsCreateDTO, NewsReadDTO
from database.core.models import News
from database.repositories.repository_depends import IDBHelper
from database.repositories.repository_depends import ISourceRepository
from database.repositories.repository_exceptions import RepositoryError


class NewsRepository:
    _model = News
    _source_repository = ISourceRepository

    def __init__(self, db_helper: IDBHelper):
        self._db_helper = db_helper

    async def bulk_create(self, dto_list: list[NewsCreateDTO], session: AsyncSession) -> list[NewsReadDTO]:
        """Создаёт записи новостей в БД."""
        news_list = [dto.model_dump(mode="json") for dto in dto_list]
        stmt = insert(self._model).values(news_list)
        stmt = stmt.on_conflict_do_nothing(index_elements=['url']).returning(self._model)
        rows = await session.execute(stmt)
        news_list = rows.scalars()
        return [NewsReadDTO(**source.__dict__) for source in news_list]

    @staticmethod
    def _get_dto(row: News) -> NewsReadDTO:
        return NewsReadDTO(**row.__dict__)

    async def get_by_user(self, dto: NewsCreateDTO, session: AsyncSession) -> NewsReadDTO | Never:
        """Создаёт запись новостного источника в БД."""
        news = self._model(**dto.model_dump())

        session.add(news)
        return news

    # async def get_users_newsfeed(
    #         self,
    #         dto: UserReadDTO,
    #         session: AsyncSession,
    #         timedelta_: timedelta = timedelta(hours=1)
    # ) -> Sequence[News]:
    #     stmt = select(self.model).filter(self.model.source.in_(dto.source), self.model.created_ad.in_...)
    #     result = await session.scalars(stmt)
    #     return result.all()
