from datetime import datetime, UTC
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .origin import Origin


class News(Base):
    __tablename__ = "news"

    title: Mapped[str] = mapped_column()
    link: Mapped[str] = mapped_column(unique=True)
    origin: Mapped["Origin"] = relationship(back_populates="news")
    created_ad: Mapped[datetime] = mapped_column(server_default=func.now(), default=datetime.now(UTC))
