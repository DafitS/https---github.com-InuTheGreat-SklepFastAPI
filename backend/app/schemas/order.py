from pydantic import BaseModel


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    user_id: int
    items: list[OrderItemCreate]

class OrderItemResponse(BaseModel):
    product_id: int
    quantity: int
    price: float

    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_price: float

    items: list[OrderItemResponse]

    class Config:
        from_attributes = True

