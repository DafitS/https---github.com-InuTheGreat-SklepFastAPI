from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import (
    UserRepository
)
from utility.enum import UserRole
from fastapi import HTTPException
from utility.password import hash_password

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
            password=hash_password(user_data.password),
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

    def change_role(
            self,
            db: Session,
            user_id: int,
            role: str
    ):
        found_user = self.get_by_id(db, user_id)

        if found_user is None:
            raise HTTPException(
                status_code=404,
                detail="Not found"
            )

        try:
            found_user.role = UserRole(role)
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Invalid role"
            )

        db.commit()
        db.refresh(found_user)

        return found_user