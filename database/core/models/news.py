from datetime import datetime, UTC
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import func, ForeignKey, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .source import Source


class News(Base):
    __tablename__ = "news"

    title: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column(unique=True)
    source_id: Mapped[UUID] = mapped_column(ForeignKey("sources.id"))
    source: Mapped["Source"] = relationship()
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),  # Установка timezone=True
        server_default=func.now(),
        default=func.now()  # Убедитесь, что здесь используется func.now()
    )
