from models import UserCreate, UserLogin, UserDisplay
from typing import Dict, Optional
from fastapi import HTTPException, status

# Placeholder for a simple in-memory "database"
users_db: Dict[str, UserDisplay] = {}

def hash_password(password: str) -> str:
    # Placeholder for password hashing
    # In a real application, use a proper cryptographic hash function
    # For example, using passlib and bcrypt
    return "hashed_" + password

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Placeholder for verifying hashed password
    return hashed_password == hash_password(plain_password)

def create_user(user: UserCreate) -> UserDisplay:
    if user.username in users_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists"
        )
    hashed_password = hash_password(user.password)
    user_db_entry = UserDisplay(
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        balance=user.initial_balance,
        id=len(users_db) + 1  # Simple way to generate a new ID
    )
    users_db[user.username] = user_db_entry
    return user_db_entry

def authenticate_user(username: str, password: str) -> Optional[UserDisplay]:
    user = users_db.get(username)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user

def get_user(username: str) -> Optional[UserDisplay]:
    return users_db.get(username)
