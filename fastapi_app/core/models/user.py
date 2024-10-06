from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user_source_association import UserSourceAssociation


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(unique=True)
    sources_details: Mapped[list["UserSourceAssociation"]] = relationship(back_populates="user")
