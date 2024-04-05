from pydantic import BaseModel

class TransferRequest(BaseModel):
    from_username: str
    to_username: str
    amount: float