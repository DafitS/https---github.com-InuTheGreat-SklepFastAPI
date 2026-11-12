from sqlalchemy.orm import Session

from app.models.category import Category


class CategoryRepository:

    def create(
        self,
        db: Session,
        name: str
    ):
        category = Category(
            name=name
        )

        db.add(category)
        db.commit()
        db.refresh(category)

        return category

    def get_all(
        self,
        db: Session
    ):
        return db.query(Category).all()