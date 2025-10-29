from fastapi import APIRouter, HTTPException
from src.application.models.partidas_models import NovaPartida
from ..persistence.partidas_repository import PartidaRepository

router = APIRouter()

partida_repo = PartidaRepository()

@router.get('/partidas/{id}')
def obter_partida(id: int):
    partida = partida_repo.obter_por_id(id)

    if not partida:
        raise HTTPException(404, 'Partida não localizada!')
    
    return partida

    

# endpoints para partidas
@router.get("/partidas")
def listar_partidas():
    return partida_repo.listar_partidas()


@router.post('/partidas', status_code=201)
def criar_partida(dados: NovaPartida):
    partida = partida_repo.adicionar_partida(dados)
    return partida


@router.delete('/partidas/{id}', status_code=204)
def remover_partida(id: int):
    partida = partida_repo.obter_por_id(id)

    if not partida:
        raise HTTPException(404, detail='Não existe essa partida!')
    
    partida_repo.remover_partida(partida)