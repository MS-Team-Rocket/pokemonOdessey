# schemas.users

from typing import List
from pydantic import BaseModel


class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config():
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    id: str
    items: List[Article] = [] # list of articles

    class Config():
        from_attributes = True

class User(BaseModel):
    id: str
    username: str

    class Config():
        from_attributes = True
