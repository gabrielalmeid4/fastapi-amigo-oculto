from typing import Optional
from pydantic import BaseModel

class Participante(BaseModel):
    id_participante: Optional[int] = None
    nome: str
    grupo_id: int
    user_id: int
    amigo_oculto_id: Optional[int] = None