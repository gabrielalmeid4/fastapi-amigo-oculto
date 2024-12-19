import asyncpg
from pydantic import ValidationError
from app.models.user import User
from app.repositories.base_repositories import BaseUserRepository
from typing import List, Optional

class UserRepositoryAsyncPg(BaseUserRepository):
    def __init__(self, db: asyncpg.Connection):
        self.db = db
        
    async def save(self, nome: str, email: str, senha: str) -> None:
        await self.db.execute(
            'INSERT INTO USERS (NOME, EMAIL, SENHA) VALUES ($1, $2, $3)',   
            nome, email, senha
        )

    async def get_by_id(self, id: int) -> Optional[User]:
        result = await self.db.fetchrow('SELECT * FROM USERS WHERE ID_USER = $1', id)
        if result:
            return User(**result)
        return None
    
    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.db.fetchrow('SELECT * FROM USERS WHERE EMAIL = $1', email)
        if result:
            return User(**result)
        return None
    
    async def get_all(self) -> Optional[List[User]]:
        result = await self.db.fetch('SELECT * FROM USERS')
        if result:
            return [User(**row) for row in result]
        return []
    
    async def remove(self, id: int) -> None:
        await self.db.execute('DELETE FROM USERS WHERE ID_USER = $1', id)
        
    async def update(self, id: int, nome: str, email: str, senha: str) -> None:
        await self.db.execute(
            'UPDATE USERS SET NOME = $1, EMAIL = $2, SENHA = $3 WHERE ID_USER = $4',
            nome, email, senha, id
        )