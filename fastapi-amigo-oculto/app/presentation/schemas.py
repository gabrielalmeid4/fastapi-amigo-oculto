from pydantic import BaseModel
from typing import Optional

class UserResponse(BaseModel):
    id_user: Optional[int] | None
    nome: str   
    email: str
    