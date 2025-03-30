from sqlalchemy.orm.session import Session
from models.articles import DbArticle
from schemas.articles import ArticleBase

# Create article
def create_article(db: Session, request: ArticleBase):
  new_article = DbArticle(
    title = request.title,
    content = request.content,
    published = request.published,
    user_id = request.creator_id
  )
  db.add(new_article)
  db.commit()
  db.refresh(new_article)
  return new_article

# Read all articles
def get_all_articles(db: Session):
  return db.query(DbArticle).all()

# Get a specific article
def get_article(db: Session, id: int):
    try:
        article = db.query(DbArticle).filter(DbArticle.id == id).first()
        if not article:
            raise Exception("Article not found")
        return article
    except Exception as e:
        return str(e)

# Update article
def update_article(db: Session, id: int, request: ArticleBase):
  article = db.query(DbArticle).filter(DbArticle.id == id)
  article.update({
    DbArticle.title: request.title,
    DbArticle.content: request.content,
    DbArticle.published: request.published
  })
  db.commit()
  return f"Article with id {id} has been updated"

# Delete article
def delete_article(db: Session, id: int):
  article = db.query(DbArticle).filter(DbArticle.id == id).first()
  db.delete(article)
  db.commit()
  return f"Article with id {id} has been deleted"