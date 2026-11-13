from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.db.base import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)

    street = Column(String(255), nullable=False)

    house_number = Column(String(20), nullable=False)

    apartment_number = Column(String(20))

    postal_code = Column(String(20), nullable=False)

    city = Column(String(100), nullable=False)

    country = Column(String(100), nullable=False)

    company_name = Column(String(255))

    tax_number = Column(String(20))

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    user = relationship(
        "User",
        back_populates="addresses"
    )