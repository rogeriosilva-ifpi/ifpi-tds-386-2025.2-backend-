from fastapi import FastAPI
from src.persistence.init_db import setup_tables
from src.presentation.partidas_controllers import router as partidas_router

app = FastAPI()

# criar tabelas
setup_tables()

@app.get("/hello")
def hello():
    return "Tá ok!"


# Incluir os Routers
app.include_router(partidas_router)