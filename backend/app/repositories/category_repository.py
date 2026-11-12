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

    def delete_by_id(
    self,
    db: Session,
    category_id: int
    ):
        result = (
            db.query(Category)
            .filter(Category.id == category_id)
            .delete()
        )

        db.commit()

        return result

    def update(
    self,
    db: Session,
    category_id: int,
    name: str
    ):
        category = db.query(Category).filter(
            Category.id == category_id
        ).first()

        if category is None:
            return None

        category.name = name

        db.commit()
        db.refresh(category)

        return category
