import uuid
import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import DateTime, func
from src.models.db.application import Application
from src.repository.table import Base


class Job(Base):
    __tablename__ = 'jobs'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(sqlalchemy.String(30))
    description: Mapped[str] = mapped_column(sqlalchemy.String(255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=True
    )
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('users.id'))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=True
    )

    user: Mapped["User"] = relationship(  # type: ignore
        back_populates='jobs',
        cascade='all'
    )
    applications: Mapped[list[Application]] = relationship(
        back_populates='job',
        cascade='all, delete-orphan'
    )
