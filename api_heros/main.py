from fastapi import FastAPI
from persistence.database import init_db
from presentation.controller_hero import router

app = FastAPI()

init_db()

app.include_router(router=router)