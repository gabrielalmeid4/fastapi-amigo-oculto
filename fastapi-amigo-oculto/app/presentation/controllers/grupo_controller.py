from fastapi import APIRouter, HTTPException, Depends
from app.models.grupo import Grupo
from app.repositories.grupo_repository import GrupoRepositoryAsyncPg
from app.repositories.participante_repository import ParticipanteRepositoryAsyncPg
from app.services.grupo_service import GrupoService
from app.config.config import get_db
from asyncpg import Connection
from app.authentication.authentication import AuthenticatorOAuth2

router = APIRouter()

def get_grupo_service(db: Connection = Depends(get_db)) -> GrupoService:
    grupo_repository = GrupoRepositoryAsyncPg(db)  
    participante_repository = ParticipanteRepositoryAsyncPg(db) 
    return GrupoService(grupo_repository, participante_repository)

@router.post("/", response_model=Grupo)
async def criar_grupo(nome: str, administrador: int, 
                       grupo_service: GrupoService = Depends(get_grupo_service)):
    try:
        return await grupo_service.criar_grupo(nome, administrador)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/sorteio/{id_grupo}", response_model=dict)
async def sorteio(id_grupo: int, 
                  grupo_service: GrupoService = Depends(get_grupo_service),
                  administrador_id: int = Depends(AuthenticatorOAuth2().get_user_from_token)):
    try:
        resultado_sorteio = await grupo_service.sorteio(id_grupo, administrador_id)
        return {"resultado": resultado_sorteio}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
