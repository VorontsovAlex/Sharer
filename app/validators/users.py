from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    """
    Common attributes shared between UserCreate and UserUpdate models.
    """
    email: str
    hashed_password: str
    is_active: Optional[bool] = True


class UserCreate(UserBase):
    """
    Pydantic model for creating a new user.
    """
    pass


class UserUpdate(UserBase):
    """
    Pydantic model for updating an existing user.
    """
    pass
