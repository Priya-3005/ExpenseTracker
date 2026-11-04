from fastapi import FastAPI
from app.api.home import router as home_router
from app.api.users import router as user_router
from app.api.expenses import router as expense_router

app = FastAPI(
    title="Expense Manager API",
    version="1.0.0"
)

app.include_router(home_router)
app.include_router(user_router)
app.include_router(expense_router)