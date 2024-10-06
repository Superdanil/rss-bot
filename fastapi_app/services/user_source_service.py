from core.dtos import UserReadDTO, SourceReadDTO
from core.dtos.user_source_dto import UserSourceDTO
from core.models import DatabaseHelper
from services import UserService, SourceService


class UserInteractor:
    def __init__(self, user_service: UserService, source_service: SourceService, db_helper: DatabaseHelper):
        self._user_service = user_service
        self._source_service = source_service
        self._db_helper = db_helper

    async def add_or_get_association(self, dto: UserSourceDTO):
        async with self._db_helper.session_getter() as session:
            user: UserReadDTO = await self._user_service.get_user(dto.telegram_id, session)
            source: SourceReadDTO = await self._source_service.add_or_get_source(dto.source, session)
            await self._user_service.add_association(user.id, source.id, session)
            await self._db_helper.commit(session)
