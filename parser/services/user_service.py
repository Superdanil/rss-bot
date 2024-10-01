from parser.core.dtos.user_dto import UserCreateDTO
from .service_depends import IUserRepository
from ..exceptions import AlreadyExistError


class UserService:
    """Класс работы с пользователями."""

    def __init__(self, repository: IUserRepository):
        self.repository = repository

    async def create(self, dto: UserCreateDTO):
        """Создаёт запись пользователя в БД."""
        try:
            return await self.repository.create(dto=dto)
        except AlreadyExistError:
            raise AlreadyExistError("User already exist")
