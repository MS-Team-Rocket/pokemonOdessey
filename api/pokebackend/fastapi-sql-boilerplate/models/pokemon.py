import uuid
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db.database import Base
from sqlalchemy import Column


class Pokemon(Base):
    __tablename__ = 'pokemons'
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    Name = Column(String, nullable=False)
    Form = Column(String, nullable=True)
    Type1 = Column(String, nullable=False)
    Type2 = Column(String, nullable=True)
    Total = Column(Integer, nullable=False)
    HP = Column(Integer, nullable=False)
    Attack = Column(Integer, nullable=False)
    Defense = Column(Integer, nullable=False)
    Sp_Atk = Column(Integer, nullable=False)
    Sp_Def = Column(Integer, nullable=False)
    Speed = Column(Integer, nullable=False)
    Generation = Column(Integer, nullable=False)