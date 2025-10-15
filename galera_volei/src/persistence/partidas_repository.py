from src.application.models.partidas_models import Partida

class PartidaRepository():
    def __init__(self):
        self.partidas:list[Partida] = [
            Partida(id=1, )
        ]

    def adicionar_partida(self, partida: Partida):
        # Código de Banco de Dados (ORM, SQLModel, SQL Alchemy, etc)
        self.partidas.append(partida)

    def listar_partidas(self):
        return self.partidas