from sqlmodel import Session, select
from src.application.models.partidas_models import NovaPartida, Partida
from src.persistence.init_db import get_engine

class PartidaRepository():
    def __init__(self):
        self.engine = get_engine()

    def adicionar_partida(self, partida: NovaPartida):
        nova_partida = Partida(arena=partida.arena,
                               local=partida.local,
                               qtd_max_participantes=partida.qtd_max_participantes,
                               qtd_min_participantes=partida.qtd_min_participantes,
                               idade_maxima=partida.idade_maxima,
                               idade_minima=partida.idade_minima,
                               cota=partida.cota,
                               data=partida.data)

        with Session(self.engine) as session:
            session.add(nova_partida)
            session.commit()
            session.refresh(nova_partida)
        
        return nova_partida
        

    def obter_por_id(self, id: int):
        with Session(self.engine) as cursor:
            partida = cursor.get(Partida, id)
            return partida


    def listar_partidas(self):
        session = Session(self.engine)
        sttm = select(Partida)
        partidas = session.exec(sttm).fetchall()
        return partidas
    

    def remover_partida(self, partida: Partida):
        with Session(self.engine) as session:
            session.delete(partida)
            session.commit()
