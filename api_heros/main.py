from fastapi import FastAPI
from persistence.database import init_db
from persistence.repository import RepositoryCameraRaiz, RepositoryCameraSQLModel
from presentation.controller_hero import router

app = FastAPI()

init_db()

repo = RepositoryCameraRaiz()
# repo = RepositoryCameraSQLModel()

app.include_router(router=router)