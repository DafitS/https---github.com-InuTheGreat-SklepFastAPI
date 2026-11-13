from fastapi import FastAPI

from app.api.router import api_router

from app.db.base import Base
from app.db.database import engine

from app.models.product import Product
from app.models.category import Category
from app.models.address import Address
from app.models.user import User

app = FastAPI(title="Products API")

Base.metadata.create_all(bind=engine)

app.include_router(api_router)