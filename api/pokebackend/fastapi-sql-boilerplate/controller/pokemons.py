from sqlalchemy.orm.session import Session
from models.pokemon import Pokemon
from schemas.pokemon import PokemonBase
from sqlalchemy.sql.expression import func


# Read all pokemon
def get_all_pokemon(db: Session):
  return db.query(Pokemon).all()

# Get a specific article
def get_pokemon(db: Session, id: int):
    try:
        article = db.query(Pokemon).filter(Pokemon.id == id).first()
        if not article:
            raise Exception("Article not found")
        return article
    except Exception as e:
        return str(e)

# Get a random pokemon
def get_random_pokemon(db: Session):
    return db.query(Pokemon).order_by(func.random()).first()
