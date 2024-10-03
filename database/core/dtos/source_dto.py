from uuid import UUID

from pydantic import BaseModel


class SourceCreateDTO(BaseModel):
    url: str


class SourceReadDTO(SourceCreateDTO):
    id: UUID
