from fastapi import FastAPI, HTTPException
from src.repository.table import Base
from src.database import engine
from src.utilities.exceptions import http_exception_handler
from src.routes.endpoints import endpoint_router


app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(router=endpoint_router)

app.add_exception_handler(HTTPException, http_exception_handler)
