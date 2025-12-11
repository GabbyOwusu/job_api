
from src.database import engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    except Exception as e:
        print(e)
        db.rollback()
        raise e
    finally:
        db.close()

