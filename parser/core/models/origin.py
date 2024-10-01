from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user_origin_association import UserOriginAssociation


class Origin(Base):
    __tablename__ = "origins"

    rss_link: Mapped[str] = mapped_column(unique=True)
    users_details: Mapped[list["UserOriginAssociation"]] = relationship(back_populates="origin")
