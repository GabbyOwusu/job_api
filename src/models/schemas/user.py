from pydantic import BaseModel, Field, EmailStr
from uuid import UUID
from typing import Literal


class UserSchema(BaseModel):
    id: UUID
    first_name: str | None
    last_name: str | None
    email: str
    user_type: str | None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    user_type: Literal['seeker', 'employer']
    first_name: str
    last_name: str


class UserWithTokenSchema(BaseModel):
    token: str
    user: UserSchema


# "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzRhYjI1YTUtYzBmMi00YTQ3LWI4NmItN2QyZmEzYTI5YzI4IiwiZXhwIjoxNzY1OTI1NzM4fQ.JZY_HQyVZE3f2ZXJoR8BtPHntZJONTugXFaCcXDdZSI"
