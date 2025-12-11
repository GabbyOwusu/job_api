from src.repository.table import Base
import uuid
import sqlalchemy
from sqlalchemy.orm import Mapped, mapped_column


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
