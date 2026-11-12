from decimal import Decimal

from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    quantity: int
    price: Decimal
    is_active: bool = True
    category_id: int


class ProductResponse(BaseModel):
    id: int
    name: str
    quantity: int
    price: Decimal
    is_active: bool
    category_id: int

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    name: str
    quantity: int
    price: float
    is_active: bool
    category_id: int