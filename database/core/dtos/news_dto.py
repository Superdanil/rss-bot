from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from database.core.dtos import OriginDTO


class NewsDTO(BaseModel):
    title: str
    link: str
    origin: OriginDTO
