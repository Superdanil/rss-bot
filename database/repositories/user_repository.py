from sqlalchemy.exc import IntegrityError

from parser.core.dtos.user_dto import UserCreateDTO
from parser.core.models import User
from .repository_depends import IAsyncSession
from ..exceptions import AlreadyExistError


# async def get_all_users(session: AsyncSession) -> Sequence[User]:
#     stmt = select(User).order_by(User.id)
#     result = await session.scalars(stmt)
#     return result.all()

class UserRepository:
    model = User

    def __init__(self, db_session: IAsyncSession):
        self._session = db_session

    async def create(self, dto: UserCreateDTO) -> User:
        """Создаёт запись пользователя в БД."""
        user = self.model(**dto.model_dump())
        self._session.add(user)
        try:
            await self._session.commit()
        except IntegrityError:
            raise AlreadyExistError(f"User with telegram_id={user.telegram_id} already exist")
        await self._session.refresh(user)
        return user
