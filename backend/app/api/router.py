from fastapi import APIRouter

from app.api.routes.product import (router as product_router)
from app.api.routes.category import (router as category_router)
from app.api.routes.user import router as user_router
from app.api.routes.address import router as address_router
from app.api.routes.order import (router as order_router)
from app.api.routes.auth import (router as auth_router)
api_router = APIRouter()

api_router.include_router(product_router)
api_router.include_router(category_router)
api_router.include_router(user_router)
api_router.include_router(address_router)
api_router.include_router(order_router)
api_router.include_router(auth_router)