from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Never

from database.core.dtos.source_dto import SourceDTO
from database.core.models import Source
from database.repositories.repository_exceptions import RepositoryError


class SourceRepository:
    model = Source

    async def create(self, dto: SourceDTO, session: AsyncSession) -> Source | Never:
        """Создаёт запись новостного источника в БД."""
        source = self.model(**dto.model_dump())
        try:
            session.add(source)
            return source
        except SQLAlchemyError as e:
            print(e)
            raise RepositoryError

    async def get_by_url(self, url: str, session: AsyncSession) -> Source | None | Never:
        """Получить источник по URL. Если не найдено - вернет None."""
        try:
            query = select(self.model).where(self.model.url == url)
            result = await session.execute(query)
            return result.scalar_one()

        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            print(e)
            raise RepositoryError
