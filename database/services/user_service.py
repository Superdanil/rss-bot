from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from .service_depends import IUserRepository, IUserSourceAssociationRepository
from ..core.dtos import UserReadDTO
from ..repositories import IDBHelper


class UserService:
    """Класс работы с пользователями."""

    def __init__(
            self,
            repository: IUserRepository,
            user_source_assoc_repository: IUserSourceAssociationRepository,
            db_helper: IDBHelper,
    ):
        self._repository = repository
        self._user_source_assoc_repository = user_source_assoc_repository
        self._db_helper = db_helper

    async def add_or_get_user(self, telegram_id: int) -> UserReadDTO:
        """Создаёт запись пользователя в БД или возвращает существующего."""

        async with self._db_helper.session_getter() as session:
            new_user = await self.get_user(telegram_id, session)
            await self._db_helper.commit(session)
            return new_user

    async def add_association(self, user_id: UUID, source_id: UUID, session) -> None:
        existing_association = await self._user_source_assoc_repository.get_association(user_id, source_id, session)

        if existing_association:
            return None

        await self._user_source_assoc_repository.add_news(user_id, source_id, session)

    async def get_user(self, telegram_id: int, session: AsyncSession) -> UserReadDTO:
        """Получает запись пользователя в БД."""

        existing_user = await self._repository.get_by_telegram_id(telegram_id, session)
        if existing_user:
            return existing_user

        return await self._repository.add_news(telegram_id, session)
