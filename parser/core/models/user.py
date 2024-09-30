from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user_origin_association import UserOriginAssociation


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(unique=True, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(unique=True)
    origins_details: Mapped[list["UserOriginAssociation"]] = relationship(back_populates="user")
