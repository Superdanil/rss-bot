from uuid import UUID

from .service_depends import ISourceRepository, IUserSourceAssociationRepository
from database.core.dtos.source_dto import SourceDTO
from database.repositories import IDBHelper
from database.repositories import RepositoryError


class SourceService:
    """Класс работы с источниками новостей."""

    def __init__(
            self,
            repository: ISourceRepository,
            user_source_repository: IUserSourceAssociationRepository,
            db_helper: IDBHelper,
    ):
        self._repository = repository
        self._user_source_repository = user_source_repository
        self._db_helper = db_helper

    async def add_or_get_source(self, dto: SourceDTO) -> SourceDTO:
        """Создаёт запись источника новостей в БД или возвращает существующий."""
        try:
            async with self._db_helper.session_getter() as session:
                existing_source = await self._repository.get_by_telegram_id(dto.url, session)
                if existing_source:
                    return existing_source

                new_source = await self._repository.create(dto, session)
                await self._db_helper.commit(session)
                return new_source

        except RepositoryError as e:
            raise e

    # async def create_user_relation(self, user_id: UUID, source_id: UUID) -> UUID:
    #     try:
    #         async with self._db_helper.session_getter() as session:
    #             existing_source = await self._user_source_repository.get_by_telegram_id(dto.url, session)
