from sqlalchemy import select, insert
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Never

from database.core.dtos import UserCreateDTO, UserReadDTO
from database.core.models import User
from database.repositories import RepositoryError


class UserRepository:
    _model = User

    async def create(self, telegram_id: int, session: AsyncSession) -> UserReadDTO | Never:
        """Создаёт запись новостного источника в БД."""
        try:
            stmt = insert(self._model).values(telegram_id=telegram_id).returning(self._model)
            result = await session.execute(stmt)
            result = result.scalar_one()
            return UserReadDTO(**result.__dict__)
        except SQLAlchemyError as e:
            print(e)
            raise RepositoryError

    async def get_by_telegram_id(self, telegram_id: int, session: AsyncSession) -> UserReadDTO | None | Never:
        """Получить пользователя по telegram_id. Если не найдено - вернет None."""
        try:
            query = select(self._model).filter(self._model.telegram_id == telegram_id)
            result = await session.execute(query)
            result = result.scalar_one()
            return UserReadDTO(**result.__dict__)

        except NoResultFound:
            print("Пользователя не найдено")
            return None
        except SQLAlchemyError as e:
            print(e)
            raise RepositoryError
