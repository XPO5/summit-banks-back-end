from fastapi import APIRouter
from src.models.transfer_model import TransferRequest

router = APIRouter()

@router.post("/transfer")
async def transfer(request: TransferRequest):
    # Placeholder for transfer logic
    out_string = f"Transfer successful from {request.from_username} to {request.to_username} for {request.amount}"
    return {"message": out_string}