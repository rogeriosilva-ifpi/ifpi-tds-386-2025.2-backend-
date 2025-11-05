from fastapi import APIRouter
from sqlmodel import Session, select
from persistence.database import get_engine

from domain.heros import Hero
from persistence.repository_hero import RepositoryHero


router = APIRouter()

repo_hero = RepositoryHero()

@router.get('/heros')
def list_heros(skip: int | None = 0, 
               take: int | None = 10,
               order: str | None = 'id'):
  
  return repo_hero.all(order, skip, take)
  

@router.post('/heros', status_code=201)
def create_hero(new_hero: Hero):
  return repo_hero.create(new_hero)