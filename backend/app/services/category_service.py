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

    def delete_by_id(
                self,
                db: Session,
                category_id: int
        ):
            return repository.delete_by_id(
                db,
                category_id
            )

    def update(
    self,
    db: Session,
    category_id: int,
    name: str
    ):
        return repository.update(
            db,
            category_id,
            name
        )