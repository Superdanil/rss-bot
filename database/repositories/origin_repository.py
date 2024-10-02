from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from parser.core.dtos.origin_dto import OriginDTO
from parser.core.models import Origin
from .repository_depends import IAsyncSession
from ..exceptions import AlreadyExistError


class OriginRepository:
    model = Origin

    def __init__(self, db_session: IAsyncSession):
        self._session = db_session

    async def create(self, dto: OriginDTO) -> Origin:
        """Создаёт запись новостного источника в БД."""
        origin = self.model(**dto.model_dump())
        self._session.add(origin)
        try:
            await self._session.commit()
        except IntegrityError:
            raise AlreadyExistError("")
        await self._session.refresh(origin)
        return origin
