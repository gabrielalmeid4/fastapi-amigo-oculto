from datetime import timedelta
from app.models.user import User
from app.repositories.base_repositories import BaseUserRepository
from app.providers.base_token import BaseTokenProvider
from app.providers.base_hash import BaseHashProvider
from app.presentation.exceptions.user_exceptions import HTTPEmailAlreadyExists
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

class UserService:
    def __init__(self, user_repository: BaseUserRepository, token_provider: BaseTokenProvider, hash_provider: BaseHashProvider):
        self.user_repository = user_repository
        self.token_provider = token_provider
        self.hash_provider = hash_provider

    async def registrar_user(self, nome: str, email: str, senha: str) -> User:     
        if await self.user_repository.get_by_email(email):
            raise HTTPEmailAlreadyExists()
        await self.user_repository.save(nome, email, senha) 
        user_created = await self.user_repository.get_by_email(email)
        hashed_password = await self.hash_provider.hash_password(senha)
        return User(id_user=user_created.id_user, nome=nome, email=email, senha=hashed_password)
    async def login(self, email: str, senha: str) -> str:
        user: User = await self.user_repository.get_by_email(email)
        if user and self.hash_provider.verify_password(senha, user.senha):
            token = await self.token_provider.create_token({user.id}, SECRET_KEY, ALGORITHM, timedelta(minutes=30))
            return token
       