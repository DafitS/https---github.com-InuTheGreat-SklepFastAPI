from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import (
    UserRepository
)

from app.schemas.user import (
    UserCreate,
    UserUpdate
)

repository = UserRepository()


class UserService:

    def create(
        self,
        db: Session,
        user_data: UserCreate
    ):

        user = User(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            password=user_data.password,
            phone=user_data.phone
        )

        return repository.create(
            db,
            user
        )

    def get_all(
        self,
        db: Session
    ):
        return repository.get_all(db)

    def get_by_id(
        self,
        db: Session,
        user_id: int
    ):
        return repository.get_by_id(
            db,
            user_id
        )

    def delete_by_id(
        self,
        db: Session,
        user_id: int
    ):
        return repository.delete_by_id(
            db,
            user_id
        )

    def update(
        self,
        db: Session,
        user_id: int,
        user_data: UserUpdate
    ):
        return repository.update(
            db,
            user_id,
            user_data
        )