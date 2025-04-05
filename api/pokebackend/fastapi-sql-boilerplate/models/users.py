import uuid
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db.database import Base
from sqlalchemy import Column, Table

# Association table for many-to-many relationship
user_pokedex = Table(
    'user_pokedex',
    Base.metadata,
    Column('user_id', String, ForeignKey('users.id'), primary_key=True),
    Column('pokemon_id', Integer, ForeignKey('pokemons.ID'), primary_key=True)
)

class DbUser(Base):
  __tablename__ = 'users'
  id = Column(String, primary_key=True, index=True, unique=True, default=str(uuid.uuid4()))
  username = Column(String)
  email = Column(String)
  password = Column(String)
  items = relationship('DbArticle', back_populates='user')
  pokedex = relationship('Pokemon', secondary=user_pokedex, back_populates='users')