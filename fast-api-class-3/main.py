from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from database import engine, get_db
from schemas import  TodoCreate, TodoUpdate, TodoResponse
from models import Base, Todo

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Todo API", description="A simple Todo API with FastAPI and SQLAlchemy", version="1.0.0")

# create todo
@app.post(
    "/todos",
    response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED,
    )
def create_todo(payload:TodoCreate, db: Session = Depends(get_db)):
    todo = Todo(**payload.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

#read all todos
@app.get(
    "/todos",
    response_model=list[TodoResponse],
    status_code=status.HTTP_200_OK
)
def list_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()