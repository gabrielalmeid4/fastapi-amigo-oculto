from typing import Optional
from pydantic import BaseModel

class Grupo(BaseModel):
    id_grupo: Optional[int] = None
    nome: str
    administrador: int