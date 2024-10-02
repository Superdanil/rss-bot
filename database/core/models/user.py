from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user_origin_association import UserOriginAssociation


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(unique=True)
    origins_details: Mapped[list["UserOriginAssociation"]] = relationship(back_populates="user")
