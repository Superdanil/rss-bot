from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user_source_association import UserSourceAssociation


class Source(Base):
    __tablename__ = "sources"

    url: Mapped[str] = mapped_column(unique=True)
    users_details: Mapped[list["UserSourceAssociation"]] = relationship(back_populates="source")
