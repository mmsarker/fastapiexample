from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    phone: Optional[str]
    full_name: Optional[str]
    gender: Optional[str]
    password: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    phone: Optional[str]
    full_name: Optional[str]
    gender: Optional[str]
    is_active: Optional[bool]


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    phone: Optional[str]
    full_name: Optional[str]
    gender: Optional[str]
    is_active: bool
    is_verified: bool
    created_at: datetime

    class Config:
        orm_mode = True
