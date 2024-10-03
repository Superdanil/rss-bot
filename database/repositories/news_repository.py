from datetime import timedelta
from typing import Sequence, Never

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from database.core.dtos import NewsDTO, UserReadDTO
from database.core.models import News
from database.repositories import RepositoryError


class NewsRepository:
    model = News

    async def create(self, dto: NewsDTO, session: AsyncSession) -> News | Never:
        """Создаёт запись новостного источника в БД."""
        news = self.model(**dto.model_dump())
        try:
            session.add(news)
            return news
        except SQLAlchemyError as e:
            print(e)
            raise RepositoryError

    async def get_users_newsfeed(
            self,
            dto: UserReadDTO,
            session: AsyncSession,
            timedelta_: timedelta = timedelta(hours=1)
    ) -> Sequence[News]:
        stmt = select(News).filter(News.source.in_(dto.source))
        result = await session.scalars(stmt)
        return result.all()
