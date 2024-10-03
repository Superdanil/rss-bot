from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class NewsCreateDTO(BaseModel):
    title: str
    url: str
    source_id: UUID


class NewsReadDTO(NewsCreateDTO):
    created_at: datetime
