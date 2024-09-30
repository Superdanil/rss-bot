from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    telegram_id: int
    user_firstname: str
    user_lastname: str
    user_fullname: str
