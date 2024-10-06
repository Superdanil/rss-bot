from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SourceDTO(BaseModel):
    id: UUID
    url: str


class NewsDTO(BaseModel):
    title: str
    link: str
    published_at: datetime
    source_id: UUID
