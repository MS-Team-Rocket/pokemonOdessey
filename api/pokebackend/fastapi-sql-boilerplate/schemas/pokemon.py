# schemas/Pokemon_schemas.py
from pydantic import BaseModel
from .users import User

# Article inside UserDisplay (Result in the response when retrieving users from database)
class Pokemon(BaseModel):
  title: str
  content: str
  published: bool
  class Config():
    from_attributes = True

# Pokemon inside database
class PokemonBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: str

# Pokemon when retrieving Pokemons from database
class PokemonDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User # imported from users schema

    class Config():
        from_attributes = True
