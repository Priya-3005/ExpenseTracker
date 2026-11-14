from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate, ExpenseResponse
from app.services.expense_service import create_expense_service, get_all_expenses_service, get_expense_by_id_service, update_expense_service, delete_expense_service
from app.models.user import User
from app.core.auth import get_current_user

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.post("/",response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    new_expense = create_expense_service(db, expense,current_user.id)


    return new_expense
@router.get("/", response_model=list[ExpenseResponse])
def get_all_expenses(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):

    return get_all_expenses_service(db,current_user.id)

@router.get("/{expense_id}", response_model=ExpenseResponse)
def get_expense(expense_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):

    expense = get_expense_by_id_service(db, expense_id,current_user.id)
    if expense is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Expense not found"
    )

    return expense

@router.put("/{expense_id}")
def update_expense(
    expense_id: int,
    updated_expense: ExpenseUpdate,
    db: Session = Depends(get_db),current_user: User = Depends(get_current_user)
):

    expense = get_expense_by_id_service(db, expense_id,current_user.id)
    if expense is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Expense not found"
    )

    update_expense_service(db,expense, updated_expense
)

    return {
        "message": "Expense updated successfully"
    }
@router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):

    expense = get_expense_by_id_service(db, expense_id,current_user.id)

    if expense is None:
        raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Expense not found"
)

    delete_expense_service(
        db,
        expense
    )

    return {
        "message": "Expense deleted successfully"
    }

