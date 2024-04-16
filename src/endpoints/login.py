from src.models.models import LoginRequest
from src.utils.utils import loginCheck
from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login(request: LoginRequest):
    response = loginCheck(request.username, request.password)
    if response == None:
        return {"error": "Incorrect username or password"}
    return {"message": "Login successful", "balance": 100.0} 