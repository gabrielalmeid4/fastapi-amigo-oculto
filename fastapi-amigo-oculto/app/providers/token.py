from fastapi import HTTPException
import jwt
from datetime import datetime, timedelta
from app.providers.base_token import BaseTokenProvider

class TokenProviderPYJWT(BaseTokenProvider):
    def create_token(data: dict, SECRET_KEY: str, ALGORITHM: str, expires_delta: timedelta = None):
        to_encode = data.copy()
        expire = datetime.now() + (expires_delta or timedelta(minutes=30))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def verify_token(token: str, SECRET_KEY: str, ALGORITHM: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
