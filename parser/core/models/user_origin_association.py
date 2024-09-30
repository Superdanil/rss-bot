from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User
    from .origin import Origin


class UserOriginAssociation(Base):
    __tablename__ = "user_origin_association"
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "origin_id",
            name="idx_unique_user_origin",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    origin_id: Mapped[int] = mapped_column(ForeignKey("origins.id"))

    # Association between UserOriginAssociation -> User
    order: Mapped["User"] = relationship(back_populates="origins_details")
    # Association between UserOriginAssociation -> Origin
    product: Mapped["Origin"] = relationship(back_populates="users_details")
