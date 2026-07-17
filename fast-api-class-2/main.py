from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()




# Get a todo with a path parameter only, todo_id in app.get is a path param
# cos it comes from the url path
@app.get("/todos/{todo_id}")
def getTodo(todo_id: int):
    return {"todo_id": todo_id}

#Get todo with query parameter
@app.get("/todos")
def filterTodo(status: str, limit: int):
    return {"status": status,
            "limit": limit
            }

class Todo(BaseModel):
    title: str
    priority: int

@app.post("/todos")
def postTodo(todo: Todo):
    return {
            "message": "Todo created",
            "todo": todo
            }

@app.put("/todos/{todo_id}")
def updateTodo(todo_id: int, todo: Todo):
    return {
        "todo_id": todo_id,
        "todo": todo
    }