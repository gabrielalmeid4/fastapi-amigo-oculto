from fastapi import HTTPException

class HTTPInvalidToken(HTTPException):
    status_code = 401
    detail = "Token inválido ou expirado"