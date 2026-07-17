from fastapi import FastAPI, Response
from typing import Optional
from pydantic import BaseModel, Field

class ExpenseCreate(BaseModel):
    title: str
    amount: float = Field(gt=0)
    category: str
    is_paid: Optional[bool] = False

class UpdateExpense(BaseModel):
    title: Optional[str] = None
    amount: Optional[float] = Field(default = None, gt = 0)
    category: Optional[str] = None
    is_paid: Optional[bool] = None

class ExpenseResponse(BaseModel):
    title: str
    amount: float
    category: str
    is_paid: bool
    