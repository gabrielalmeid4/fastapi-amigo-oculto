from fastapi import APIRouter, HTTPException, Depends
from app.models.user import User
from app.providers.base_hash import BaseHashProvider
from app.providers.base_token import BaseTokenProvider
from app.repositories.user_repository import UserRepositoryAsyncPg
from app.services.user_service import UserService
from app.config.config import get_db
from asyncpg import Connection

router = APIRouter()

def get_user_service(db: Connection = Depends(get_db), 
                     hash_provider: BaseHashProvider = Depends(), 
                     token_provider: BaseTokenProvider = Depends()) -> UserService:
    user_repository = UserRepositoryAsyncPg(db)  
    return UserService(user_repository, token_provider, hash_provider)

@router.post("/", response_model=User)
async def registrar_user(user: User, user_service: UserService = Depends(get_user_service)):
    await user_service.registrar_user(user.nome, user.email, user.senha)
    return user


@router.post("/login", response_model=str)
async def login(email: str, senha: str, user_service: UserService = Depends(get_user_service)):
    token = await user_service.login(email, senha)
    return token