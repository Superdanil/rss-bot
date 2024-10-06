from uuid import UUID

from pydantic import BaseModel, ConfigDict


class SourceCreateDTO(BaseModel):
    url: str

    model_config = ConfigDict(from_attributes=True)


class SourceReadDTO(SourceCreateDTO):
    id: UUID
