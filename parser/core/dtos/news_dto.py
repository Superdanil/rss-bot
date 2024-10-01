from pydantic import BaseModel

from origin_dto import OriginDTO


class NewsDTO(BaseModel):
    title: str
    link: str
    origin: OriginDTO
