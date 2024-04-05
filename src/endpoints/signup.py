from fastapi import APIRouter
from models.models import SignUpRequest
from src.utils.utils import addUserIfNotExists

router = APIRouter()

@router.post("/signup")
async def signup(request: SignUpRequest):
    response = addUserIfNotExists(request.username, request.password, request.email, request.first_name, request.last_name, request.initial_balance)
    if response == None:
        return {"error": "User already exists"}
    return {"message": "User created successfully"}