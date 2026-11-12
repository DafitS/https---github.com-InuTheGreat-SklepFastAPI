from fastapi import APIRouter

from app.api.routes.product import (
    router as product_router
)

from app.api.routes.category import (
    router as category_router
)

api_router = APIRouter()

api_router.include_router(
    product_router
)

api_router.include_router(
    category_router
)