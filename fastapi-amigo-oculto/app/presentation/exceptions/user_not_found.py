from fastapi import HTTPException

class HTTPUserNotFound(HTTPException):
    status_code = 404
    detail = "Usuário não encontrado"
    
