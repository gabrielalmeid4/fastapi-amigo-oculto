import datetime

from jose import jwt

from application.providers.token_provider import TokenProvider
from core.settings import settings
from presentation.exceptions.auth_exceptions import TokenExpiredException
from presentation.exceptions.base_exceptions import AppError


class JoseTokenProvider(TokenProvider):
    def __init__(self):
        self.secret_key = settings.TOKEN_SECRET
        self.algorithm = settings.TOKEN_ALGORITHM

    def encode(self, data: dict, expires: int) -> str:
        expiration_time = datetime.datetime.now() + datetime.timedelta(seconds=expires)
        payload = {**data, "exp": expiration_time}
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def decode(self, token: str) -> str:
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except jwt.ExpiredSignatureError:
            raise TokenExpiredException()
        except jwt.JWTError as e:
            raise AppError(f"Erro ao decodificar o token: {str(e)}")
