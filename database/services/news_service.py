from ..core.dtos import NewsDTO
from .service_depends import IUserRepository
from ..exceptions import AlreadyExistError


class NewsService:
    """Класс работы с пользователями."""

    def __init__(self, repository: NewsDTO):
        self.repository = repository

    async def create(self, dto: NewsDTO):
        """Создаёт запись пользователя в БД."""
        try:
            return await self.repository.create(dto=dto)
        except AlreadyExistError:
            raise AlreadyExistError("User already exist")
