from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.category import (
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate
)
from app.services.category_service import (
    CategoryService
)

router = APIRouter(prefix="/categories", tags=["Categories"])

service = CategoryService()


@router.post(
    "/",
    response_model=CategoryResponse
)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db)
):
    return service.create(
        db,
        category.name
    )


@router.get(
    "/",
    response_model=list[CategoryResponse]
)
def get_categories(
    db: Session = Depends(get_db)
):
    return service.get_all(db)

@router.delete("/{category_id}")
def remove_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    return service.delete_by_id(db, category_id)

@router.put(
    "/{category_id}",
    response_model=CategoryResponse
)
def update_category(
    category_id: int,
    category: CategoryUpdate,
    db: Session = Depends(get_db)
):
    return service.update(
        db,
        category_id,
        category.name
    )