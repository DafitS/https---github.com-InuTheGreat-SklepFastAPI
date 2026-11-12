from sqlalchemy.orm import Session

from app.repositories.category_repository import (
    CategoryRepository
)

repository = CategoryRepository()


class CategoryService:

    def create(
        self,
        db: Session,
        name: str
    ):
        return repository.create(
            db,
            name
        )

    def get_all(
        self,
        db: Session
    ):
        return repository.get_all(db)