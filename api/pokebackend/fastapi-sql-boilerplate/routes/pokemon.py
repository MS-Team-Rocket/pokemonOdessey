from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from controller import pokemons as db_pokemon

router = APIRouter(
  prefix='/pokemon',
  tags=['pokemon']
)


# Read all articles
@router.get('/')#, response_model=List[ArticleDisplay])
def get_all_pokemons(db: Session = Depends(get_db)):
    return db_pokemon.get_random_pokemon(db)
# Get a specific article
@router.get('/{id}') #, response_model=ArticleDisplay)
def get_pokemon(id: int, db: Session = Depends(get_db)):
  return db_pokemon.get_pokemon(db, id)
  
