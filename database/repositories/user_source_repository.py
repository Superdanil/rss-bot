from typing import Never
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from database.core.models import UserSourceAssociation
from database.repositories import RepositoryError


class UserSourceAssociationRepository:
    model = UserSourceAssociation

    async def create(
            self,
            user_id: UUID,
            source_id: UUID,
            session: AsyncSession
    ) -> UserSourceAssociation | Never:
        """"""
        association = self.model(user_id=user_id, source_id=source_id)
        session.add(association)
        try:
            session.add(association)
            return association
        except SQLAlchemyError as e:
            print(e)
            raise RepositoryError

    async def get_association(
            self,
            user_id: UUID,
            source_id: UUID,
            session: AsyncSession
    ) -> UserSourceAssociation | None | Never:

        try:
            query = select(self.model).where(
                self.model.user_id == user_id,
                self.model.source_id == source_id
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()

        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            print(e)
            raise RepositoryError
