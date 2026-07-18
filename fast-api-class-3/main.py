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
# @app.get(
#     "/todos",
#     response_model=list[TodoResponse],
#     status_code=status.HTTP_200_OK
# )
# def list_todos(db: Session = Depends(get_db)):
#     return db.query(Todo).all()

#read one
@app.get("/todos/{todo_id}", response_model=TodoResponse, status_code=status.HTTP_200_OK)
def list_one_todo(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {todo_id} not found")
    return todo

#update todo
@app.put("/todos/{todo_id}", response_model=TodoResponse, status_code=status.HTTP_200_OK)
def update_todo(todo_id:int, payload: TodoUpdate, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {todo_id} not found")
    
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(todo, field, value)

    db.commit()
    db.refresh(todo)
    return todo

#delete todo
@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {todo_id} not found")
    
    db.delete(todo)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#filtering wih query params
@app.get("/todos", response_model=list[TodoResponse])
def list_todo_q(completed:bool | None = None, search:str | None = None, db: Session = Depends(get_db)):
    query = db.query(Todo)
     
    if completed is not None:
        query = query.filter(Todo.completed == completed)

    if search: 
        query = query.filter(Todo.title.ilike(f"%{search}%"))

    return query.all()

# @app.get("/todos/{todo_id}", response_model=TodoResponse)
# def list_todo_q(todo_id:int, db: Session = Depends(get_db)):
#     query = db.query(Todo)
     
#     if completed is not None:
#         query = query.filter(Todo.completed == completed)

#     return query.all()