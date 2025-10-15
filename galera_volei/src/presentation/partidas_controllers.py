from fastapi import APIRouter
from ..persistence.partidas_repository import PartidaRepository

router = APIRouter()

partida_repo = PartidaRepository()

# endpoints para partidas
@router.get("/partidas")
def listar_partidas():
    return partida_repo.listar_partidas()


@router.post('/partidas')
def criar_partida(dados: NovaPartida):
    ...