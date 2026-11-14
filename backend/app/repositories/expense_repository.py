from sqlalchemy.orm import Session

from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate


def create_expense(db: Session, expense: ExpenseCreate,user_id: int):

    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        user_id=user_id
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense

def get_all_expenses(db: Session,user_id:int):
    return db.query(Expense).filter(
        Expense.user_id == user_id
    ).all()

def get_expense_by_id(db: Session, expense_id: int,user_id:int):
    return db.query(Expense).filter(Expense.id == expense_id,Expense.user_id == user_id).first()
def update_expense(
    db: Session,    
    expense: Expense,
    updated_expense
):
    expense.title = updated_expense.title
    expense.amount = updated_expense.amount
    expense.category = updated_expense.category

    db.commit()
    db.refresh(expense)

    return expense
def delete_expense(db: Session,expense: Expense):

    if expense is None:
        return {
            "message": "Expense not found"
        }

    db.delete(expense)
    db.commit()

    return {
        "message": "Expense deleted successfully"
    }