from pydantic import BaseModel


class OriginDTO(BaseModel):
    rss_link: str
