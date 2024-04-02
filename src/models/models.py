from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str

class UserCreate(UserBase):
    password: str
    initial_balance: float

class UserDisplay(UserBase):
    id: Optional[int] = None
    balance: float

class Config:
    orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

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
