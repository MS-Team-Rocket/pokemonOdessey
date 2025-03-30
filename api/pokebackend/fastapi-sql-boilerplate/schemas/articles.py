# schemas/article_schemas.py
from pydantic import BaseModel
from .users import User

# Article inside UserDisplay (Result in the response when retrieving users from database)
class Article(BaseModel):
  title: str
  content: str
  published: bool
  class Config():
    from_attributes = True

# Article inside database
class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: str

# Article when retrieving articles from database
class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User # imported from users schema

    class Config():
        from_attributes = True
