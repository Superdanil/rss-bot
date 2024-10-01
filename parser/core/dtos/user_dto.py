from uuid import UUID

from pydantic import BaseModel

from parser.core.dtos import OriginDTO


class UserCreateDTO(BaseModel):
    telegram_id: int


class UserReadDTO(UserCreateDTO):
    id: UUID
    origins: set[OriginDTO]
