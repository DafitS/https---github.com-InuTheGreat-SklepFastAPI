from fastapi import FastAPI

from app.api.router import api_router

from app.db.base import Base
from app.db.database import engine

from app.models.product import Product
from app.models.category import Category

app = FastAPI(title="Products API")

Base.metadata.create_all(bind=engine)

app.include_router(api_router)