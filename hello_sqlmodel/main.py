from fastapi import FastAPI
from sqlmodel import Field, SQLModel, create_engine

app = FastAPI()

class Hero(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str = Field(max_length=200)

engine = create_engine('sqlite:///database.db')

SQLModel.metadata.create_all(engine)


@app.get('/')
def hello():
  return 'hello'