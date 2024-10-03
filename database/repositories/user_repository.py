from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import Never

from database.core.dtos import UserCreateDTO
from database.core.models import Source, User
from database.repositories.repository_exceptions import RepositoryError


class UserRepository:
    model = User

    async def create(self, dto: UserCreateDTO, session: AsyncSession) -> Source | Never:
        """Создаёт запись новостного источника в БД."""
        user = self.model(**dto.model_dump())
        try:
            session.add(user)
            return user
        except SQLAlchemyError as e:
            print(e)
            raise RepositoryError

    async def get_by_telegram_id(self, telegram_id: int, session: AsyncSession) -> Source | None | Never:
        """Получить пользователя по telegram_id. Если не найдено - вернет None."""
        try:
            query = select(self.model).filter(self.model.telegram_id == telegram_id)
            result = await session.execute(query)
            return result.scalar_one()

        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            print(e)
            raise RepositoryError
