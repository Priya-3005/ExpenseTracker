from fastapi import APIRouter
router = APIRouter()
@router.get("/")
def home():
    return {
        "message": "Expense Manager API is running"
    }
