from uuid import UUID

from pydantic import BaseModel


class UserCreateDTO(BaseModel):
    telegram_id: int


class UserReadDTO(UserCreateDTO):
    id: UUID
