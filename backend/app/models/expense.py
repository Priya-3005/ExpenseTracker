from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy import ForeignKey
from datetime import datetime

from app.db.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    date = Column(Date, nullable=False,default=lambda: datetime.now().strftime("%Y-%m-%d"))
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)