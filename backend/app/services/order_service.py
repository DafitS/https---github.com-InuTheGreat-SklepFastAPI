from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product

from app.repositories.order_repository import (
    OrderRepository
)


repository = OrderRepository()


class OrderService:

    def create(
        self,
        db,
        order_data
    ):

        order = Order(
            user_id=order_data.user_id
        )

        total_price = 0

        for item in order_data.items:

            product = (
                db.query(Product)
                .filter(
                    Product.id == item.product_id
                )
                .first()
            )

            if product is None:
                continue

            order_item = OrderItem(
                product_id=product.id,
                quantity=item.quantity,
                price=product.price
            )

            product.quantity -= item.quantity

            total_price += (
                product.price *
                item.quantity
            )

            order.items.append(
                order_item
            )

        order.total_price = total_price

        return repository.create(
            db,
            order
        )

    def get_all(
        self,
        db
    ):
        return repository.get_all(db)

    def get_by_id(
        self,
        db,
        order_id: int
    ):
        return repository.get_by_id(
            db,
            order_id
        )