from sqlalchemy.orm import Session

from app.models.product import Product
from app.repositories.product_repository import (
    ProductRepository
)

repository = ProductRepository()


class ProductService:

    def create(
        self,
        db: Session,
        name: str,
        quantity: int,
        price: float,
        is_active: bool,
        category_id: int
    ):

        product = Product(
            name=name,
            quantity=quantity,
            price=price,
            is_active=is_active,
            category_id=category_id
        )

        return repository.create(
            db,
            product
        )

    def get_all(
        self,
        db: Session
    ):
        return repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        product_id: int
    ):
        return repository.get_by_id(
            db,
            product_id
        )