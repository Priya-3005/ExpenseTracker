import token

from sqlalchemy.orm import Session

from app.repositories.user_repository import create_user,get_user_by_email
from app.schemas.user import UserCreate
from app.core.security import hash_password,verify_password
from app.core.auth import create_access_token


def create_user_service(
    db: Session,
    user: UserCreate
):
    user.password = hash_password(user.password)
    return create_user(db, user)
def login_user_service(
    db: Session,
    email: str,
    password: str
):

    user = get_user_by_email(
        db,
        email
    )

    if user is None:
        return None

    if not verify_password(
        password,
        user.password
    ):
        return None

    token = create_access_token({"sub": user.email})

    return token