from typing import Generic, List, TypeVar, Optional
from app.models.grupo import Grupo
from app.models.participante import Participante
from app.models.user import User

T = TypeVar('T')  

class BaseRepository(Generic[T]):
    async def save(self, entity: T) -> None:
        raise NotImplementedError

    async def get_by_id(self, id: int) -> Optional[T]:
        raise NotImplementedError
    
    async def get_all(self) -> Optional[List[T]]:
        raise NotImplementedError
    
    async def remove(self, id: int) -> None:
        raise NotImplementedError
    
    async def update(self, id: int, entity: T) -> None:
        raise NotImplementedError
    
class BaseUserRepository(BaseRepository[User]):
    async def save(self, user: User) -> None:
        raise NotImplementedError

    async def get_by_id(self, id: int) -> Optional[User]:
        raise NotImplementedError
    
    async def get_by_email(self, email: str) -> Optional[User]:
        raise NotImplementedError
    
    async def get_all(self) -> Optional[List[User]]:
        raise NotImplementedError
    
    async def remove(self, id: int) -> None:
        raise NotImplementedError
    
    async def update(self, id: int, nome: str, email: str, senha: str) -> None:
        raise NotImplementedError

    
class BaseParticipanteRepository(BaseRepository[Participante]):
    async def save(self, nome: str, user_id: int, grupo_id: int) -> None:
        raise NotImplementedError
    
    async def get_by_id(self, id: int) -> Optional[Participante]:
        raise NotImplementedError
    
    async def get_all(self) -> Optional[List[Participante]]:
        raise NotImplementedError
    async def get_by_grupo_id(self, grupo_id: int) -> Optional[List[Participante]]:
        raise NotImplementedError
    
    async def remove(self, id: int) -> None:
        raise NotImplementedError
    
    async def update(self, id: int, nome: str, amigo_oculto_id: int) -> None:
        raise NotImplementedError
    
class BaseGrupoRepository(BaseRepository[Grupo]):
    async def save(self, nome: str, administrador: int) -> None:
        raise NotImplementedError
    
    async def get_by_id(self, id: int) -> Optional[Grupo]:
        raise NotImplementedError
    
    async def get_all(self) -> Optional[List[Grupo]]:
        raise NotImplementedError
    
    async def remove(self, id: int) -> None:
        raise NotImplementedError
    
    async def update(self, id: int, nome: str, administrador: int) -> None:
        raise NotImplementedError