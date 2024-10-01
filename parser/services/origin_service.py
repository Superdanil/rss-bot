from requests import session

from parser.core.dtos.origin_dto import OriginDTO
from .service_depends import IOriginRepository


class OriginService:
    """Класс работы с источниками новостей."""

    def __init__(self, repository: IOriginRepository):
        self.repository = repository

    async def create_origin(self, origin: OriginDTO):
        """Создаёт запись источника новостей в БД."""
        try:
            origin = await self.repository.create(origin=origin)
            return origin
        except Exception:
            raise ZeroDivisionError
