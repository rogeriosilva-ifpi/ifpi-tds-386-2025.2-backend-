from fastapi import APIRouter, status, HTTPException
from schemas import Rio, NovoRio
from ulid import ULID

router = APIRouter()


rios: list[Rio] = [
  Rio(id=str(ULID()), nome='Parnaíba', extensao=1400, permanente=True),
  Rio(id=str(ULID()), nome='São Francisco', extensao=2830, permanente=True),
  Rio(id=str(ULID()), nome='Jaguaribe', extensao=633, permanente=False)
  ]


@router.get('')
def list_rios(ordem:str | None = None,
              tipo:str | None = None):
  if tipo == 'permanente':
    rios_filtrados = []
    for rio in rios:
      if rio.permanente:
        rios_filtrados.append(rio)
    
    return rios_filtrados
 
  return rios

# Path Param ou Parametro de Rota/Path
@router.get('/{id}', status_code=status.HTTP_200_OK)
def detail_rios(id:int):
  if id % 2 == 0:
    return f'Detalhes do Rio de ID = {id}'
  else:
    # return Response(content='Rio não localizado', 
    #                 status_code=status.HTTP_404_NOT_FOUND)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                  detail='Rio não localizado')


@router.post('', status_code=status.HTTP_201_CREATED)
def create_rio(dados: NovoRio):
  # como criar efetivamente um Rio no BD
  return dados


@router.put('/{id}')
def update_rio(id:int):
  # Fake.. ok?!
  return f'Rio({id}) atualizado com sucesso.'


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_rio(id:int):
  return
