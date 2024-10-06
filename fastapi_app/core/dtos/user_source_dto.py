from pydantic import BaseModel, ConfigDict


class UserSourceDTO(BaseModel):
    telegram_id: int
    source: str

    model_config = ConfigDict(from_attributes=True)
