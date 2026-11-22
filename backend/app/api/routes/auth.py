from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.db.database import get_db

from app.schemas.auth import (
    LoginRequest,
    LoginResponse
)

from app.services.auth_service import (
    AuthService
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

service = AuthService()

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    token = service.login(
        db,
        form_data.username,
        form_data.password
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }