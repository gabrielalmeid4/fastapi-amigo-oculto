import asyncpg
from pydantic import ValidationError
from app.models.grupo import Grupo
from app.repositories.base_repositories import BaseGrupoRepository
from typing import List, Optional

class GrupoRepositoryAsyncPg(BaseGrupoRepository):
    def __init__(self, db: asyncpg.Connection):

        self.db = db
        
    async def save(self, nome: str, administrador: int) -> None:
        await self.db.execute(
        'INSERT INTO GRUPOS(NOME, ADMINISTRADOR) VALUES ($1, $2)',
        nome, administrador
        )
        
    async def get_by_id(self, id: int) -> Optional[Grupo]:
        result = await self.db.fetchrow('SELECT * FROM GRUPOS WHERE ID_GRUPO = $1', id)
        if result:
            return Grupo(**result)
        return None
    
    async def get_all(self) -> Optional[List[Grupo]]:
        result = await self.db.fetch('SELECT * FROM GRUPOS')
        if result:
            return [Grupo(**row) for row in result]
        return []

    async def remove(self, id: int) -> None:
        await self.db.execute('DELETE FROM GRUPOS WHERE ID_GRUPO = $1', id)
    
    async def update(self, id: int, nome: str, administrador: int) -> None:
        
        await self.db.execute(
            'UPDATE GRUPOS SET NOME = $1, ADMINISTRADOR = $2 WHERE ID_GRUPO = $3',
            nome, administrador, id
        )