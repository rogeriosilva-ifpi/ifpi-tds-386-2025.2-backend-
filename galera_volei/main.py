from fastapi import FastAPI
from src.presentation.partidas_controllers import router as partidas_router

app = FastAPI()

@app.get("/hello")
def hello():
    return "Tá ok!"


# Incluir os Routers
app.include_router(partidas_router)