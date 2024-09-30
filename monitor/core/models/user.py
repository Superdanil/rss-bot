from monitor.core.models import Base

from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    id: Mapped[int] = mapped_column(unique=True)
    telegram_id: Mapped[int] = mapped_column(unique=True)
    user_firstname: Mapped[str] = mapped_column(unique=True)
    user_lastname: Mapped[str] = mapped_column(unique=True)
    user_fullname: Mapped[str] = mapped_column(unique=True)

    __tablename__="users"
