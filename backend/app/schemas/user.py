from pydantic import BaseModel

from utility.enum import UserRole


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    phone: str | None = None


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str | None
    role: UserRole
    is_active: bool

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    phone: str | None = None
    role: UserRole
    is_active: bool