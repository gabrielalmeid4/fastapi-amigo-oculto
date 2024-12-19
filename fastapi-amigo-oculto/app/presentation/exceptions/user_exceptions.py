from fastapi import HTTPException

class HTTPUserNotFound(HTTPException):
    def __init__(self, status_code= 404, detail =  "Usuário não encontrado", headers = None):
        super().__init__(status_code, detail, headers)

class HTTPEmailAlreadyExists(HTTPException):
    def __init__(self, status_code= 400, detail =  "E-mail já cadastrado", headers = None):
        super().__init__(status_code, detail, headers)
    
    