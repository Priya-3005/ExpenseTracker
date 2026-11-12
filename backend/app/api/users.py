from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.db.database import get_db
from app.schemas.user import UserCreate,UserResponse,UserLogin
from app.services.user_service import create_user_service,login_user_service
from app.core.auth import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    new_user = create_user_service(
    db,
    user)

    return new_user 
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    token = login_user_service(
    db,
    form_data.username,
    form_data.password
)

    if token is None:
        return {
            "message": "Invalid email or password"
        }

    return {
        "access_token": token,
        "token_type": "bearer"
    }
@router.get("/me")
def get_me(
    current_user: str = Depends(get_current_user)
):

    return {
        "email": current_user
    }   