from sqlmodel import create_engine, SQLModel

def get_engine():
  # engine = create_engine('sqlite:///database.db')
  engine = create_engine('sqlite:///database.db')
  return engine


def setup_tables():
  engine = get_engine()
  SQLModel.metadata.create_all(engine)