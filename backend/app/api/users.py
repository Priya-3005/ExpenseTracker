from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate,UserResponse,UserLogin
from app.services.user_service import create_user_service,login_user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    new_user = create_user_service(
    db,
    user)

    return new_user 
@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    logged_in_user = login_user_service(
        db,
        user.email,
        user.password
    )

    if logged_in_user is None:
        return {
            "message": "Invalid email or password"
        }

    return {
        "message": "Login successful"
    }