from uuid import UUID

from database.core.models import UserSourceAssociation
from database.repositories import IDBHelper, RepositoryError
from database.routers.router_depends import IUserService, ISourceService
from database.services.service_depends import IUserSourceAssociationRepository


class UserInteractor:

    def __init__(
            self,
            user_service: IUserService,
            source_service: ISourceService,
            repository: IUserSourceAssociationRepository,
            db_helper: IDBHelper
    ):
        self._user_service = user_service
        self._source_service = source_service
        self._repository = repository
        self._db_helper = db_helper

    async def add_or_get_association(self, user_id: UUID, source_id: UUID):
        try:
            async with self._db_helper.session_getter() as session:
                existing_association = await self._repository.get_association(user_id, source_id, session)

            if existing_association:
                return existing_association
            new_association = UserSourceAssociation(user_id=user_id, source_id=source_id)
            await self._db_helper.commit(session)
            return new_association

        except RepositoryError as e:
            raise e
