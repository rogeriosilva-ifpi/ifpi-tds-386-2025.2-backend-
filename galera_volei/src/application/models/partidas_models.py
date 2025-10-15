from pydantic import BaseModel
from typing import Literal



class PartidaBase(BaseModel):
    data: str | None
    local: str
    arena: str
    qtd_min_participantes: int
    qtd_max_participantes: int | None
    idade_minima: int
    idade_maxima: int | None
    cota: float
    nivel: Literal['iniciante', 'intermediario', 'avancado']
    categoria: Literal['masculino', 'feminino', 'misto']


class Partida(PartidaBase):
    id: int


class NovaPartida(PartidaBase):
    ...