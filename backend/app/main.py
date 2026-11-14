from fastapi import FastAPI
from app.api.home import router as home_router
from app.api.users import router as user_router
from app.api.expenses import router as expense_router
from app.exceptions.handlers import expense_not_found_handler, user_not_found_handler, invalid_credentials_handler, generic_exception_handler
from app.exceptions.custom_exceptions import ExpenseNotFoundException, UserNotFoundException, InvalidCredentialsException

app = FastAPI(
    title="Expense Manager API",
    version="1.0.0"
)
app.add_exception_handler(
    ExpenseNotFoundException,
    expense_not_found_handler
)
app.add_exception_handler(
    UserNotFoundException,
    user_not_found_handler
)
app.add_exception_handler(
    InvalidCredentialsException,
    invalid_credentials_handler
)
app.add_exception_handler(
    Exception,
    generic_exception_handler
)

app.include_router(home_router)
app.include_router(user_router)
app.include_router(expense_router)