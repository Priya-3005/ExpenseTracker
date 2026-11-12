from pydantic import BaseModel,Field
from datetime import date


class ExpenseCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=2, max_length=50)    

class ExpenseUpdate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=2, max_length=50)
class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    date: date
    user_id: int

    class Config:
        from_attributes = True