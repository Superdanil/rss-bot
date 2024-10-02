from datetime import timedelta
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from .repository_depends import IAsyncSession
from ..core.dtos import NewsDTO, UserReadDTO
from ..core.models import News
from ..exceptions import AlreadyExistError


class NewsRepository:
    model = News

    def __init__(self, db_session: IAsyncSession):
        self._session = db_session

    async def create(self, dto: NewsDTO) -> News:
        """Создаёт запись пользователя в БД."""
        news = self.model(**dto.model_dump())
        self._session.add(news)
        try:
            await self._session.commit()
        except IntegrityError:
            raise AlreadyExistError("already exist")
        await self._session.refresh(news)
        return news

    async def get_users_newsfeed(self, dto: UserReadDTO, timedelta_: timedelta = timedelta(hours=1)) -> Sequence[News]:
        stmt = select(News).filter(News.origin.in_(dto.origins))
        result = await self._session.scalars(stmt)
        return result.all()
