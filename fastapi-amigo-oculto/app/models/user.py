from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id_user: Optional[int] = None
    nome: str
    email: str
    senha: str