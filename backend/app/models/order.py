from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Numeric
)

from sqlalchemy.orm import relationship

from app.db.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    total_price = Column(
        Numeric(10, 2),
        default=0
    )

    user = relationship(
        "User",
        back_populates="orders"
    )

    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )