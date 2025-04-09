from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from routes import blog_get
# from routes import blog_post
from routes import users
from routes import articles
from routes import pokemon
from db.database import engine
from models import articles as article_model
from models import users as user_model


app = FastAPI()

# ✅ Add CORS middleware here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development. Replace with your extension ID in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(articles.router)
app.include_router(pokemon.router)
# app.include_router(blog_get.router)
# app.include_router(blog_post.router)

@app.get('/')
def index():
  return {'message': 'Hello Pokemon fans!'}

# create new DB or load the existing
article_model.Base.metadata.create_all(engine)
user_model.Base.metadata.create_all(engine)