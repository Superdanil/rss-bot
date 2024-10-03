from sqlalchemy import select, insert
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Never

from database.core.dtos import SourceReadDTO
from database.core.dtos.source_dto import SourceCreateDTO
from database.core.models import Source
from database.repositories.repository_exceptions import RepositoryError


class SourceRepository:
    _model = Source

    async def create(self, source: str, session: AsyncSession) -> SourceReadDTO | Never:
        """Создаёт запись новостного источника в БД."""
        try:
            stmt = insert(self._model).values(source=source).returning(self._model)
            result = await session.execute(stmt)
            result = result.scalar_one()
            return SourceReadDTO(**result.__dict__)
        except SQLAlchemyError as e:
            raise RepositoryError

    async def get_sources(self, session: AsyncSession, limit: int, offset: int) -> list[SourceReadDTO] | Never:
        """Получить источники по limit и offset. Если не найдено - вернет None."""

        query = select(self._model).limit(limit).offset(offset).order_by(self._model.id)
        row = await session.execute(query)
        result = row.scalars()
        return [SourceReadDTO(**source.__dict__) for source in result]

    async def get_by_url(self, url: str, session: AsyncSession) -> SourceReadDTO | None | Never:
        """Получить источник по URL. Если не найдено - вернет None."""
        try:
            query = select(self._model).where(self._model.url == url)
            row = await session.execute(query)
            result = row.scalar_one()
            return SourceReadDTO(**result.__dict__)

        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            raise RepositoryError(e)
