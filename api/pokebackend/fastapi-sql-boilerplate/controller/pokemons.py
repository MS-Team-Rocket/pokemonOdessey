from sqlalchemy.orm.session import Session
from models.pokemon import Pokemon
from schemas.pokemon import PokemonBase
from sqlalchemy.sql.expression import func

EXCLUDED_IDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 152, 25, 26, 144, 145, 146, 149, 150, 151]

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

def get_random_pokemon(db: Session):
    return (
        db.query(Pokemon)
        .filter(Pokemon.ID >= 1, Pokemon.ID <= 151)
        .filter(~Pokemon.ID.in_(EXCLUDED_IDS))  # Exclude specific IDs
        .order_by(func.random())
        .first()
    )
