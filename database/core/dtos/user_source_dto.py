from pydantic import BaseModel


class UserSourceDTO(BaseModel):
    telegram_id: int
    source: str
