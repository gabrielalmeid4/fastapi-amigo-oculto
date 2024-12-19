from fastapi import Header, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.authentication.base_authentication import BaseAuthenticator
from jwt import decode, ExpiredSignatureError, DecodeError
from dotenv import load_dotenv
from app.presentation.exceptions.invalid_token import HTTPInvalidToken
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="authentication")

class AuthenticatorOAuth2(BaseAuthenticator):
    def get_user_from_token(token: str = Depends(oauth2_scheme)) -> int:
        try:
            payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return int(payload.get("sub"))
        except (ExpiredSignatureError, DecodeError):
            raise HTTPInvalidToken()
            # raise HTTPException(status_code=401, detail="Token inválido ou expirado")