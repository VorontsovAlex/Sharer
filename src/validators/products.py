from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    title: str
    description: Optional[str]
    owner_id: int
    category_id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass
