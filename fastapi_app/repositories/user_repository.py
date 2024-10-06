from sqlalchemy import select, insert
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Never

from core.dtos import UserReadDTO
from core.models import User
from exceptions import RepositoryError
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    _model = User

    async def create(self, telegram_id: int, session: AsyncSession) -> UserReadDTO | Never:
        """Создаёт запись новостного источника в БД."""
        stmt = insert(self._model).values(telegram_id=telegram_id).returning(self._model)
        try:
            result = await session.execute(stmt)
            result = result.scalar_one()
            return self._get_dto(result, UserReadDTO)

        except SQLAlchemyError as e:
            raise RepositoryError(e)

    async def get_by_telegram_id(self, telegram_id: int, session: AsyncSession) -> UserReadDTO | None | Never:
        """Получить пользователя по telegram_id. Если не найдено - вернет None."""
        query = select(self._model).filter(self._model.telegram_id == telegram_id)
        try:
            result = await session.execute(query)
            result = result.scalar_one()
            return self._get_dto(result, UserReadDTO)

        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            raise RepositoryError(e)
