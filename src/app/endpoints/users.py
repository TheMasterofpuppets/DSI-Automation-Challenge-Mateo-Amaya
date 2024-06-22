from fastapi import Depends, APIRouter, HTTPException, status
from ..auth.token_manager import db, encode_token
from pydantic import BaseModel


router = APIRouter()

class User(BaseModel):
    username: str
    password: str


def authenticate(username: str, password: str) -> dict | None:
    if username in db and db[username]["password"] == password:
        return {"username": username}
    return None

@router.post("/login", response_model=dict)
async def login(credential: User):
    """
    Endpoint to authenticate a user and issue an access token.

    Parameters:
    - credential: User - User credentials (username and password).

    Returns:
    - dict: Dictionary containing an access token and token type.
    """
    user = authenticate(credential.username,credential.password)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = encode_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}