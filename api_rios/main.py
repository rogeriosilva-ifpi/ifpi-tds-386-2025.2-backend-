from fastapi import FastAPI
from routes_cidades import router as cidades_router
from routes_rios import router as rios_router

app = FastAPI()

app.include_router(cidades_router)
app.include_router(rios_router, prefix='/rivers')

