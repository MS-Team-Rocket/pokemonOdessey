from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# change this to your desired database URL (MySQL, PostgreSQL, etc.)
SQLALCHEMY_DATABASE_URL = "sqlite:///./master.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    Returns a database session.

    This function creates a new database session using the `SessionLocal` class. 
    The session is then yielded to the caller, allowing them to perform database operations. 
    Once the caller is done with the session, it should be closed using the `db.close()` method.

    Returns:
        A database session object.

    Example usage:
        db = get_db()
        # Perform database operations using `db`
        db.close()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()