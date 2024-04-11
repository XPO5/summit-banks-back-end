from fastapi import FastAPI, HTTPException, status, Body
from src.models.models import LoginRequest, SignUpRequest
from src.endpoints import healthcheck, signup, transfer
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Summit Banks App")

# Configure CORS
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def login(request: LoginRequest):
    # Placeholder for user authentication logic
    return {"message": "Login successful", "balance": 100.0}  # Example balance

@app.patch("/change_user_info")
async def change_user_info(request: SignUpRequest):
    # Placeholder for user info update logic
    return {"message": "User info updated successfully"}

@app.get("/metrics")
async def metrics():
    # Placeholder for metrics retrieval logic
    return {"metrics": "placeholder"}

app.include_router(healthcheck.router)
app.include_router(signup.router)
app.include_router(transfer.router)