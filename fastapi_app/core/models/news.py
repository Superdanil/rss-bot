from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .source import Source


class News(Base):
    __tablename__ = "news"

    title: Mapped[str] = mapped_column()
    link: Mapped[str] = mapped_column(unique=True)
    published_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))
    source_id: Mapped[UUID] = mapped_column(ForeignKey("sources.id"))
    source: Mapped["Source"] = relationship()
