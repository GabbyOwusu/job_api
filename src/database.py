from dotenv import load_dotenv
import os
from sqlalchemy import create_engine 

load_dotenv()


db_url = os.getenv('DATABASE_URL')

DB_NAME = os.getenv("DATABASE_NAME")
DB_PASS = os.getenv("DATABASE_PASSWORD")
DB_HOST = os.getenv("DATABASE_HOST")
DB_PORT = os.getenv("DATABASE_PORT")

DATABASE_URL = (
    f"postgresql://postgres:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_engine(DATABASE_URL)
