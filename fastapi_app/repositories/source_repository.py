from sqlalchemy import select, insert
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Never

from core.dtos import SourceReadDTO
from core.models import Source
from exceptions import RepositoryError
from repositories.base_repository import BaseRepository


class SourceRepository(BaseRepository):
    _model = Source

    async def create(self, source: str, session: AsyncSession) -> SourceReadDTO | Never:
        """Создаёт запись новостного источника в БД."""
        stmt = insert(self._model).values(url=source).returning(self._model)
        try:
            result = await session.execute(stmt)
            result = result.scalar_one()
            return self._get_dto(result, SourceReadDTO)

        except SQLAlchemyError as e:
            raise RepositoryError(e)

    async def get_sources(self, session: AsyncSession, limit: int, offset: int) -> list[SourceReadDTO] | Never:
        """Получить источники по limit и offset. Если не найдено - вернет None."""
        query = select(self._model).limit(limit).offset(offset).order_by(self._model.id)
        try:
            row = await session.execute(query)
            result = row.scalars()
            return [self._get_dto(source, SourceReadDTO) for source in result]

        except SQLAlchemyError as e:
            raise RepositoryError(e)

    async def get_by_url(self, url: str, session: AsyncSession) -> SourceReadDTO | None | Never:
        """Получить источник по URL. Если не найдено - вернет None."""
        query = select(self._model).where(self._model.url == url)
        try:
            row = await session.execute(query)
            result = row.scalar_one()
            return self._get_dto(result, SourceReadDTO)

        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            raise RepositoryError(e)
