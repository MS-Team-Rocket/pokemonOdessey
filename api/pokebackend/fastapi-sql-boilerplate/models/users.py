import uuid
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from db.database import Base
from sqlalchemy import Column


class DbUser(Base):
  __tablename__ = 'users'
  id = Column(String, primary_key=True, index=True, unique=True, default=str(uuid.uuid4()))
  username = Column(String)
  email = Column(String)
  password = Column(String)
  items = relationship('DbArticle', back_populates='user')