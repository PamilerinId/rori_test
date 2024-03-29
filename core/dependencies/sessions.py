from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.env import config
  
  
engine = create_engine(  
    config.WRITER_DB_URL
)  


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
