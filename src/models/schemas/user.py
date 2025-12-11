from pydantic import BaseModel, Field, EmailStr
from uuid import UUID


class UserSchema(BaseModel):
    id: UUID
    first_name: str | None
    last_name: str | None
    email: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserWithTokenSchema(BaseModel):
    token: str
    user: UserSchema
