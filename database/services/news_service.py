from .service_depends import INewsRepository
from database.core.dtos import NewsDTO
from database.exceptions import AlreadyExistError


class NewsService:
    """Класс работы с новостями."""

    def __init__(self, repository: INewsRepository):
        self.repository = repository

    async def create(self, dto: NewsDTO):
        """Создаёт запись новости в БД."""
        try:
            return await self.repository.create(dto=dto)
        except AlreadyExistError:
            raise AlreadyExistError("News already exist")
