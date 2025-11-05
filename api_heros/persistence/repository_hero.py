from sqlmodel import Session, select
from domain.heros import Hero
from persistence.database import get_engine


class RepositoryHero():

  def __init__(self):
    self.engine = get_engine()

  def all(self, order: str, offset: int, limit: int):
    with Session(self.engine) as session:
      statement = select(Hero).order_by(order).offset(offset).limit(limit)
      return session.exec(statement).fetchall()
    
  
  def create(self, data: Hero):
    with Session(self.engine) as session:
      session.add(data)
      session.commit()
      
      session.refresh(data)

      return data
  