
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import (
    create,
    get_by_email,
)


class EmailAlreadyRegisteredError(Exception):
    pass


def register_user(
    db: Session,
    email: str,
    password: str,
) -> User:
    existing_user = get_by_email(db, email)

    if existing_user is not None:
        raise EmailAlreadyRegisteredError(
            "Email is already registered"
        )

    user = User(
        email=email,
        password_hash=hash_password(password),
    )

    return create(db, user)
