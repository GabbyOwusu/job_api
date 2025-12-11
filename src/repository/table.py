from sqlalchemy.orm import DeclarativeBase
from typing import Type
import sqlalchemy


class DBTable(DeclarativeBase):
    metadata: sqlalchemy.MetaData = sqlalchemy.MetaData()


Base: Type[DeclarativeBase] = DBTable
