from ast import Try
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelos
class Rio(BaseModel):
  id: int
  nome: str
  extensao: float
  permanente: bool


rios: list[Rio] = [
  Rio(id=1, nome='Parnaíba', extensao=1400, permanente=True),
  Rio(id=2, nome='São Francisco', extensao=2830, permanente=True),
  Rio(id=3, nome='Jaguaribe', extensao=633, permanente=False)
  ]



@app.get('/rios')
def list_rios(ordem: str | None = None,
              tipo:str | None = None):
  if tipo == 'permanente':
    rios_filtrados = []
    for rio in rios:
      if rio.permanente:
        rios_filtrados.append(rio)
    return rios_filtrados

  if ordem:
    rios_ordenados = sorted(rios, key=lambda x:x[ordem])
    return rios_ordenados

  return rios


@app.get('/rios/{id}')
def detail_rios(id:int):
  return f'Detalhes do Rio de ID = {id}'


