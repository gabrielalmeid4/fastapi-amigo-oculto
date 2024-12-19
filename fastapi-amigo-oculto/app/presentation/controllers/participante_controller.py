from fastapi import APIRouter, HTTPException, Depends
from app.models.participante import Participante
from app.repositories.grupo_repository import GrupoRepositoryAsyncPg
from app.repositories.participante_repository import ParticipanteRepositoryAsyncPg
from app.services.participante_service import ParticipanteService
from app.config.config import get_db
from asyncpg import Connection
from app.authentication.authentication import AuthenticatorOAuth2 

router = APIRouter()

def get_participante_service(db: Connection = Depends(get_db)) -> ParticipanteService:
    participante_repository = ParticipanteRepositoryAsyncPg(db)  
    grupo_repository = GrupoRepositoryAsyncPg(db)  
    return ParticipanteService(participante_repository, grupo_repository)

@router.post("/", response_model=Participante)
async def registrar_participante(participante: Participante, 
                                 participante_service: ParticipanteService = Depends(get_participante_service),
                                 user_id: int = Depends(AuthenticatorOAuth2().get_user_from_token)):  
    try:
        return await participante_service.registrar_participante(participante.grupo_id, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/quem_presentear/{id_grupo}/{id_participante}", response_model=str)
async def quem_presentear(id_grupo: int, id_participante: int, 
                          participante_service: ParticipanteService = Depends(get_participante_service),
                          user_id: int = Depends(AuthenticatorOAuth2().get_user_from_token)): 
    try:
        return await participante_service.quem_presentear(id_grupo, id_participante, user_id)
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erro ao acessar o presenteado")