from fastapi import FastAPI
from app.presentation.controllers.user_controller import router as user_router
from app.presentation.controllers.grupo_controller import router as grupo_router
from app.presentation.controllers.participante_controller import router as participante_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(participante_router, prefix="/participantes", tags=["participantes"])
app.include_router(grupo_router, prefix="/grupos", tags=["grupos"])
