from .database import Base, engine
from sqlalchemy import Column, Integer, String

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    description = Column(String, unique=False)
    
# Inicjalizacja bazy danych
Base.metadata.create_all(bind=engine)