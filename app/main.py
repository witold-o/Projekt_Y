from fastapi import FastAPI
from fastapi import Depends
from typing import List


from app import crud
from app import schemas
from app import models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Inicjalizacja bazy danych
models.Base.metadata.create_all(bind=engine)

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
print("XDDDDDDDDDDDDDDDDD")
print(DB_USER)
print(DB_PORT)
print(DB_PASSWORD)
print(DB_PORT)
app = FastAPI()


# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.get("/tasks/", response_model=List[schemas.Task])
def get_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)
