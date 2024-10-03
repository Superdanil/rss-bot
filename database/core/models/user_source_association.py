from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User
    from .source import Source


class UserSourceAssociation(Base):
    __tablename__ = "user_source_association"
    __table_args__ = (UniqueConstraint("user_id", "source_id", name="idx_unique_user_source"))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id"))

    # Association between UserSourceAssociation -> User
    user: Mapped["User"] = relationship(back_populates="sources_details")
    # Association between UserSourceAssociation -> Source
    source: Mapped["Source"] = relationship(back_populates="users_details")
