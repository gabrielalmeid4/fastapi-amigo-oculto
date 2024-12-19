import random
from typing import List
from app.models.grupo import Grupo
from app.models.participante import Participante
from app.repositories.base_repositories import BaseGrupoRepository, BaseParticipanteRepository

class GrupoService:
    def __init__(self, grupo_repository: BaseGrupoRepository, participante_repository: BaseParticipanteRepository):
        self.grupo_repository = grupo_repository
        self.participante_repository = participante_repository

    async def criar_grupo(self, nome: str, administrador: int) -> Grupo:
        await self.grupo_repository.save(nome, administrador)
        return Grupo(nome=nome, administrador=administrador)

    async def sorteio(self, id_grupo: int, administrador_id: int) -> None:
        grupo_a_sortear: Grupo = await self.grupo_repository.get_by_id(id_grupo)
        if not grupo_a_sortear:
            raise ValueError("Grupo não encontrado.")
        
        if grupo_a_sortear.administrador != administrador_id:
            raise ValueError("Somente o administrador do grupo pode realizar o sorteio.")
        
        participantes: List[Participante] = await self.participante_repository.get_by_grupo_id(id_grupo)
        if not participantes:
            raise ValueError("Nenhum participante encontrado no grupo.")
        
        caixa_de_sorteio = []
        
        for participante in participantes:
            caixa_de_sorteio.append(participante.id_participante)
        
        while len(caixa_de_sorteio) > 0:   
            for participante in participantes:
                amigo_sorteado_id = caixa_de_sorteio[(random.randint(0, len(caixa_de_sorteio) - 1))]
                if amigo_sorteado_id != participante.id_participante:
                    caixa_de_sorteio.remove(amigo_sorteado_id)
                    await self.participante_repository.update(participante.id_participante, amigo_sorteado_id)