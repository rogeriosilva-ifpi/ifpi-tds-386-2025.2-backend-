from sqlmodel import SQLModel, Field



class PartidaBase(SQLModel):
    data: str | None
    local: str
    arena: str = Field(nullable=False, max_length=180)
    qtd_min_participantes: int
    qtd_max_participantes: int | None
    idade_minima: int
    idade_maxima: int | None
    cota: float
    # nivel: Literal['iniciante', 'intermediario', 'avancado']
    # categoria: Literal['masculino', 'feminino', 'misto']


class Partida(PartidaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class NovaPartida(PartidaBase):
    ...