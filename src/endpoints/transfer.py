from fastapi import APIRouter
from src.models.transfer_model import TransferRequest
from src.utils.utils import transferFunds

router = APIRouter()

@router.post("/transfer")
async def transfer(request: TransferRequest):
    response = transferFunds(request.from_username, request.to_username, request.amount)
    if not response:
        return {"error": "Transfer failed"}
    out_string = f"Transfer successful from {request.from_username} to {request.to_username} for {request.amount}"
    return {"message": out_string}