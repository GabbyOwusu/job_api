from src.repository.table import Base
import uuid
import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import DateTime, func
from src.models.db.application import Application


class User(Base):
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
    )
    first_name: Mapped[str] = mapped_column(
        sqlalchemy.String(30), nullable=True)
    last_name: Mapped[str] = mapped_column(
        sqlalchemy.String(30), nullable=True)
    email:  Mapped[str] = mapped_column(sqlalchemy.String(30), unique=True)
    password: Mapped[str] = mapped_column(sqlalchemy.String(1024), unique=True)
    user_type: Mapped[str] = mapped_column(
        sqlalchemy.String(30), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=True
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=True
    )
    jobs: Mapped[list['Job']] = relationship(  # type: ignore
        back_populates='user',
        cascade='all, delete-orphan',
    )
    applications: Mapped[list[Application]] = relationship(
        back_populates='user',
        cascade='all, delete-orphan'
    )
