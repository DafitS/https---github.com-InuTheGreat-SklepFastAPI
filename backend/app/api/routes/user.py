from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse
)

from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

service = UserService()


@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return service.create(db, user)


@router.get("/", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db)
):
    return service.get_all(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = service.get_by_id(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    user = service.update(
        db,
        user_id,
        user_data
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    result = service.delete_by_id(
        db,
        user_id
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted"
    }