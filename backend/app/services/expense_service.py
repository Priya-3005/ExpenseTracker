from sqlalchemy.orm import Session

from app.repositories.expense_repository import create_expense, get_all_expenses, get_expense_by_id, update_expense, delete_expense
from app.schemas.expense import ExpenseCreate


def create_expense_service(
    db: Session,
    expense: ExpenseCreate,user_id: int
):
    return create_expense(db, expense,user_id)
def get_all_expenses_service(db: Session):
    return get_all_expenses(db)
def get_expense_by_id_service(
    db: Session,
    expense_id: int
):
    return get_expense_by_id(db, expense_id)
def update_expense_service(
    db: Session,
    expense,
    updated_expense
):
    return update_expense(db, expense, updated_expense)
def delete_expense_service(db,expense):
    delete_expense(db, expense)