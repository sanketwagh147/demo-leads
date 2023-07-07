from config import settings
from sqlalchemy import create_engine

# from sqlalchemy.ext.declarative import declarative_base
from base_class import Base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = f"mysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = Base()


def get_db_con():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
