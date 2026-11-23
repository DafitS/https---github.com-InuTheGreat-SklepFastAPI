from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.security import oauth2_scheme

from app.db.database import get_db

from app.repositories.user_repository import (
    UserRepository
)
from utility.enum import UserRole
from fastapi import HTTPException, Depends

from utility.jwt import decode_token


repository = UserRepository()

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    try:
        payload = decode_token(token)

        user_id = payload["sub"]

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = repository.get_by_id(
        db,
        int(user_id)
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user

def require_admin(
    current_user = Depends(get_current_user)
):

    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return current_user