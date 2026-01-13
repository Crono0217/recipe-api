from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./recipes.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session_Local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




