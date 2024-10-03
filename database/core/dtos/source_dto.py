from pydantic import BaseModel


class SourceDTO(BaseModel):
    url: str
