from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class NewsResponseDTO(BaseModel):
    title: str
    link: str

    model_config = ConfigDict(from_attributes=True)


class NewsCreateDTO(NewsResponseDTO):
    source_id: UUID
    published_at: datetime = Field(..., description="Timestamp with time zone")


class NewsReadDTO(NewsCreateDTO):
    id: UUID
