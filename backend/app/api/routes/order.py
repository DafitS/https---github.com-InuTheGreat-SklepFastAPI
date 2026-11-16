from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.order import (
    OrderCreate,
    OrderResponse
)

from app.services.order_service import (
    OrderService
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

service = OrderService()

@router.post(
    "/",
    response_model=OrderResponse
)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):
    return service.create(
        db,
        order
    )

@router.get(
    "/",
    response_model=list[OrderResponse]
)
def get_orders(
    db: Session = Depends(get_db)
):
    return service.get_all(db)

@router.get(
    "/{order_id}",
    response_model=OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = service.get_by_id(
        db,
        order_id
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order

