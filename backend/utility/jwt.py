from datetime import datetime
from datetime import timedelta

from jose import jwt


SECRET_KEY = "super-secret-key"

ALGORITHM = "HS256"

ACCESS_TOKEN_MINUTES = 60

def create_access_token(
    user_id: int
):

    payload = {
        "sub": str(user_id),
        "exp": datetime.utcnow()
        + timedelta(
            minutes=ACCESS_TOKEN_MINUTES
        )
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def decode_token(token: str):
    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )