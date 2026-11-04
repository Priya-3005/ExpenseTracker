from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate,UserResponse
from app.services.user_service import create_user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse,status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    new_user = create_user_service(
    db,
    user)

    return new_user 