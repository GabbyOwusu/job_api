from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from src.models.schemas.user import UserSchema


class JobSchema(BaseModel):
    id: UUID
    title: str
    description: str
    created_at: datetime


class JobCreate(BaseModel):
    title: str
    description: str


class JobUpdate(BaseModel):
    id: UUID
    title: str | None
    description: str | None


class ApplicationSchema(BaseModel):
    id: UUID
    user: UserSchema
    job: JobSchema
