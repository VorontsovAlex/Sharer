from pydantic import BaseModel
from typing import Optional


class OrderBase(BaseModel):
    email: str
    hashed_password: str
    is_active: Optional[bool] = True


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass
