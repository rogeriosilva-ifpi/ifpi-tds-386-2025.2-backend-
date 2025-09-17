from ast import Try
from pydantic import BaseModel
from ulid import ULID

class CidadeBase(BaseModel):
  nome: str
  estado: str
  populacao: int


class Cidade(CidadeBase):
  id: str | None = str(ULID())
  pib: float = 0.0


class NovaCidade(CidadeBase):
  pass



class RioBase(BaseModel):
  nome: str
  extensao: float


class Rio(RioBase):
  id: str | None = None
  permanente: bool = True


class NovoRio(RioBase):
  pass