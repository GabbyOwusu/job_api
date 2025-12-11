import sqlalchemy
from sqlalchemy.orm import Session


class BaseCRUDRepository:
    def __init__(self, session: Session):
        self.session = session
