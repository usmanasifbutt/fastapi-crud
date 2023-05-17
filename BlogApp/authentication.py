from jose import JWTError, jwt
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta

SECRET_KEY = "a72d007077f61cc77d29277fe6017b139258ca65f9bf562bcaa77ccd9221e9e1"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None


def create_access_token(data: dict):
    to_ecode =  data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_ecode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_ecode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email= email)
    except JWTError:
        raise credentials_exception