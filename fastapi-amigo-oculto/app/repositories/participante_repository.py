import asyncpg
from pydantic import ValidationError
from app.models.participante import Participante
from app.repositories.base_repositories import BaseParticipanteRepository
from typing import List, Optional

class ParticipanteRepositoryAsyncPg(BaseParticipanteRepository):
    def __init__(self, db: asyncpg.Connection):
        self.db = db
        
    async def save(self, nome: str, user_id: int, grupo_id: int) -> None:
        await self.db.execute(
            'INSERT INTO PARTICIPANTES (NOME, USER_ID, GRUPO_ID, AMIGO_OCULTO_ID) VALUES ($1, $2, $3, NULL)',   
            nome, user_id, grupo_id
        )
        
    async def get_by_id(self, id: int) -> Optional[Participante]:
        result = await self.db.fetchrow('SELECT * FROM PARTICIPANTES WHERE ID_PARTICIPANTE = $1', id)
        if result:
            return Participante(**result)
        return None
    
    async def get_by_grupo_id(self, grupo_id: int) -> Optional[List[Participante]]:
        result = await self.db.fetch('SELECT * FROM PARTICIPANTES WHERE GRUPO_ID = $1', grupo_id)
        if result:
            return [Participante(**row) for row in result]
        return []
    
    async def get_all(self) -> Optional[List[Participante]]:
        result = await self.db.fetch('SELECT * FROM PARTICIPANTES')
        if result:
            return [Participante(**row) for row in result]
        return []

    async def remove(self, id: int) -> None:
        await self.db.execute('DELETE FROM PARTICIPANTES WHERE ID_PARTICIPANTE = $1', id)
    
    async def update(self, id: int, amigo_oculto_id: int) -> None:
        await self.db.execute(
            'UPDATE PARTICIPANTES SET AMIGO_OCULTO_ID = $1 WHERE ID_PARTICIPANTE = $2',
            amigo_oculto_id, id
        )