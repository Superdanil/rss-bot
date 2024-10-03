from uuid import UUID

from pydantic import BaseModel

from database.core.dtos import SourceDTO


class UserCreateDTO(BaseModel):
    telegram_id: int


class UserReadDTO(UserCreateDTO):
    id: UUID
    origins: set[SourceDTO]
