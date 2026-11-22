from app.repositories.user_repository import (
    UserRepository
)

from utility.password import (
    verify_password
)

from utility.jwt import (
    create_access_token
)

repository = UserRepository()


class AuthService:

    def login(
        self,
        db,
        email,
        password
    ):

        user = repository.get_by_email(
            db,
            email
        )

        if not user:
            return None

        valid = verify_password(
            password,
            user.password
        )

        if not valid:
            return None

        token = create_access_token(
            user.id
        )

        return token