from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str

class UserCreate(UserBase):
    password: str
    initial_balance: float = Field(..., ge=0, description="Initial deposit must be non-negative")

class UserDisplay(UserBase):
    id: Optional[int] = None
    balance: float

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

class Transfer(BaseModel):
    from_username: str
    to_username: str
    amount: float = Field(..., gt=0, description="Transfer amount must be greater than zero")

# You might also want to define a model for the response of operations
# For example, a simple operation result that could be used for login, transfer, etc.
class OperationResult(BaseModel):
    message: str
    details: Optional[str] = None
