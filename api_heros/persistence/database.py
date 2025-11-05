from sqlmodel import create_engine, SQLModel


# Configurar o Banco de Dados
def get_engine():
  return create_engine('sqlite:///heros.db')


# Criar as Tabelas no Banco de Dados
def init_db():
  SQLModel.metadata.create_all(get_engine())