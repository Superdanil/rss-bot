from .service_depends import IUserRepository
from ..core.dtos import UserCreateDTO
from ..repositories import IDBHelper
from ..repositories import RepositoryError


class UserService:
    """Класс работы с пользователями."""

    def __init__(self, repository: IUserRepository, db_helper: IDBHelper):
        self._repository = repository
        self._db_helper = db_helper

    async def add_or_get_user(self, dto: UserCreateDTO) -> UserCreateDTO:
        """Создаёт запись пользователя в БД или возвращает существующего."""
        try:
            async with self._db_helper.session_getter() as session:
                existing_user = await self._repository.get_by_telegram_id(dto.telegram_id, session)
                if existing_user:
                    return existing_user

                new_user = await self._repository.create(dto, session)
                await self._db_helper.commit(session)
                return new_user

        except RepositoryError as e:
            raise e
