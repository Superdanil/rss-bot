from pydantic import BaseModel

from database.core.dtos.source_dto import SourceDTO


class NewsDTO(BaseModel):
    title: str
    url: str
    origin: SourceDTO
