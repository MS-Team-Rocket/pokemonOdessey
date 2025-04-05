from utils.hash import Hash
from sqlalchemy.orm.session import Session
from schemas.users import UserBase
from models.users import DbUser

# Create user
def create_user(db: Session, request: UserBase):
  new_user = DbUser(
    username = request.username,
    email = request.email,
    password = Hash.bcrypt(request.password)
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

# Read all users
def get_all_users(db: Session):
  return db.query(DbUser).all()

# Get a specific user
def get_user(db: Session, id: int):
  return db.query(DbUser).filter(DbUser.id == id).first()

# Update user
def update_user(db: Session, id: int, request: UserBase):
  user = db.query(DbUser).filter(DbUser.id == id)
  user.update({
    DbUser.username: request.username,
    DbUser.email: request.email,
    DbUser.password: Hash.bcrypt(request.password)
  })
  db.commit()
  return f"User with id {id} has been updated"

# Delete user
def delete_user(db: Session, id: int):
  user = db.query(DbUser).filter(DbUser.id == id).first()
  db.delete(user)
  db.commit()
  return f"User with id {id} has been deleted"