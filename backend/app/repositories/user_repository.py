from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserUpdate


class UserRepository:

    def create(
        self,
        db: Session,
        user: User
    ):
        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    def get_all(
        self,
        db: Session
    ):
        return db.query(User).all()

    def get_by_id(
        self,
        db: Session,
        user_id: int
    ):
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def delete_by_id(
        self,
        db: Session,
        user_id: int
    ):
        user = self.get_by_id(
            db,
            user_id
        )

        if user is None:
            return False

        db.delete(user)
        db.commit()

        return True

    def update(
        self,
        db: Session,
        user_id: int,
        user_data: UserUpdate
    ):
        user = self.get_by_id(
            db,
            user_id
        )

        if user is None:
            return None

        user.first_name = user_data.first_name
        user.last_name = user_data.last_name
        user.email = user_data.email
        user.password = user_data.password
        user.phone = user_data.phone
        user.role = user_data.role
        user.is_active = user_data.is_active

        db.commit()
        db.refresh(user)

        return user