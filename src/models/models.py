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

class SignUpRequest(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    initial_balance: float

class LoginRequest(BaseModel):
    username: str
    password: str

class TransferRequest(BaseModel):
    to_username: str
    amount: float

class UpdateInformationRequest(BaseModel):
    to_update: str

class OperationResult(BaseModel):
    message: str
    details: Optional[str] = None
