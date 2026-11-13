from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Enum as SqlEnum
)

from sqlalchemy.orm import relationship

from app.db.base import Base
from utility.enum import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(100), nullable=False)

    last_name = Column(String(100), nullable=False)

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )

    phone = Column(String(20))

    role = Column(
        SqlEnum(UserRole),
        nullable=False,
        default=UserRole.STANDARD
    )

    is_active = Column(
        Boolean,
        default=True
    )

    addresses = relationship(
        "Address",
        back_populates="user",
        cascade="all, delete-orphan"
    )