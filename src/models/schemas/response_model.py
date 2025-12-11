from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel

T = TypeVar('T')


class ErrorSchema(BaseModel):
    message: str
    code: str


class ResponseSchema(BaseModel, Generic[T]):
    status: str
    message: str
    data: Optional[T] = None
    error: Optional[ErrorSchema] = None
