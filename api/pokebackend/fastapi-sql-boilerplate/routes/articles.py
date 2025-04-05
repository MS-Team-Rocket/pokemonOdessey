from typing import List
from schemas.articles import ArticleBase, ArticleDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from controller import articles as db_article

router = APIRouter(
  prefix='/article',
  tags=['article']
)

# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
  return db_article.create_article(db, request)

# Read all articles
@router.get('/')#, response_model=List[ArticleDisplay])
def get_all_articles(db: Session = Depends(get_db)):
    return db_article.get_all_articles(db)

# Get a specific article
@router.get('/{id}') #, response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
  return db_article.get_article(db, id)
  

# Update article
@router.post('/{id}/update')
def update_article(id: int, request: ArticleBase, db: Session = Depends(get_db)):
  return db_article.update_article(db, id, request)

# Delete article
@router.delete('/{id}')
def delete_article(id: int, db: Session = Depends(get_db)):
    return db_article.delete_article(db, id)