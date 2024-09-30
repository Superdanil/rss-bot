from pydantic import BaseModel


class UserCreate(BaseModel):
    telegram_id: int


class UserRead(UserCreate):
    subscriptions: set
