from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.product import (
    ProductCreate,
    ProductResponse
)

from app.services.product_service import (
    ProductService
)

router = APIRouter(prefix="/products", tags=["Products"])

service = ProductService()


@router.post(
    "/",
    response_model=ProductResponse
)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    return service.create(
        db,
        product.name,
        product.quantity,
        product.price,
        product.is_active,
        product.category_id
    )


@router.get(
    "/",
    response_model=list[ProductResponse]
)
def get_products(
    db: Session = Depends(get_db)
):
    return service.get_all(db)