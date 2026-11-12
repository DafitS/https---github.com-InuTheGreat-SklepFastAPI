from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:

    def create(
        self,
        db: Session,
        product: Product
    ):
        db.add(product)
        db.commit()
        db.refresh(product)

        return product

    def get_all(
        self,
        db: Session
    ):
        return db.query(Product).all()

    def get_by_id(
        self,
        db: Session,
        product_id: int
    ):
        return (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

    def delete_by_id(
        self,
        db: Session,
        product_id: int   
    ):
        return (
            db.query(Product)
            .filter(Product.id == product_id)
            .delete()
        )

    def delete_by_id(
    self,
    db: Session,
    product_id: int
    ):
        product = db.query(Product).filter(
            Product.id == product_id
        ).first()

        if product is None:
            return None

        db.delete(product)
        db.commit()

        return product

    def update(
    self,
    db: Session,
    product_id: int,
    name: str,
    quantity: int,
    price: float,
    is_active: bool,
    category_id: int
    ):
        product = db.query(Product).filter(
            Product.id == product_id
        ).first()

        if product is None:
            return None

        product.name = name
        product.quantity = quantity
        product.price = price
        product.is_active = is_active
        product.category_id = category_id

        db.commit()
        db.refresh(product)

        return product