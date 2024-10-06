from uuid import UUID

from pydantic import BaseModel, ConfigDict


class UserCreateDTO(BaseModel):
    telegram_id: int

    model_config = ConfigDict(from_attributes=True)


class UserReadDTO(UserCreateDTO):
    id: UUID
