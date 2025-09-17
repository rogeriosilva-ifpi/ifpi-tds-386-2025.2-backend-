from fastapi import APIRouter
from schemas import Cidade, NovaCidade
from ulid import ULID

router = APIRouter()

cidades = []
city1 = Cidade(id=str(ULID()), nome='Capitão Campos', estado='PI', populacao=7800)
cidades.append(city1)

@router.get('/cidades')
def list_cidades():
  return cidades


@router.post('/cidades', status_code=201)
def create_cidades(dados: NovaCidade):
  cidade = Cidade(
                # id=str(ULID()), 
                  nome=dados.nome, 
                  estado=dados.estado,
                  populacao=dados.populacao)
  
  cidades.append(cidade)
  return cidade


# Detalhes
  # Buscar pelo ID e retonar o Objeto num (200)
  # ou 404 se nao existir

# Alterar
# def update_cidade(id:str, dados:AlterarCidade):
  # buscar a cidade pelo id
  # se nao achar returnar 404
  # se achar altera os atributos que vieram
  # return a cidade alterada (200)
  ...

# Remover
  # buscar pelo id que chegou na rota/path
  # returnar o 404 sse nao achar
  # ou remover efetivamente se achar
  # returnar um (204)

