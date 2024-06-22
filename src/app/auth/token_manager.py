import secrets

from jose import JWTError, jwt
from fastapi import Depends, status, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

db = {"admin": {"username":"admin","password":"password"},
      "juan": {"username":"juan","password":"12345"}}

SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"

def encode_token(data: dict) -> str:
    token = jwt.encode(data,SECRET_KEY,ALGORITHM)
    return token

def get_current_user(token: str = Depends(security)):
    try:
        decode = jwt.decode(token.credentials,SECRET_KEY,algorithms=[ALGORITHM])
        username: str = decode.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        if username not in db:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return db[username]
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")