# External Modules
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Internal Modules
# from databases import Database

DB_URL = "mysql+pymysql://root:73538862@localhost:3306/pidb"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
def get_pidb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()