from app.models.grupo import Grupo
from app.models.participante import Participante
from app.models.user import User
from app.repositories.base_repositories import (
    BaseGrupoRepository,
    BaseParticipanteRepository,
    BaseUserRepository,
)


class ParticipanteService:
    def __init__(
        self,
        participante_repository: BaseParticipanteRepository,
        user_repository: BaseUserRepository,
        grupo_repository: BaseGrupoRepository,
    ):
        self.participante_repository = participante_repository
        self.user_repository = user_repository
        self.grupo_repository = grupo_repository

    async def registrar_participante(self, grupo_id: int, user_id: int) -> Participante:
        novo_participante: User = await self.user_repository.get_by_id(user_id)
        if not novo_participante:
            raise ValueError("Usuário não encontrado.")

        grupo: Grupo = await self.grupo_repository.get_by_id(grupo_id)
        if not grupo:
            raise ValueError("Grupo não encontrado.")

        if grupo.administrador != user_id:
            raise ValueError(
                "Você não tem permissão para adicionar participantes a este grupo."
            )

        await self.participante_repository.save(
            novo_participante.nome, novo_participante.id_user, grupo_id
        )
        return Participante(grupo_id=grupo_id, user_id=user_id)

    async def quem_presentear(self, id_grupo: int, id_participante: int, id_user: int):
        participante: Participante = await self.participante_repository.get_by_id(
            id_participante
        )

        if participante.user_id != id_user:
            raise ValueError("Você não pode acessar os dados de outro participante.")

        amigo_oculto_id = participante.amigo_oculto_id

        if amigo_oculto_id is None:
            return None

        amigo_oculto: Participante = await self.participante_repository.get_by_id(
            amigo_oculto_id
        )

        if amigo_oculto is None:
            return None

        return amigo_oculto.nome
