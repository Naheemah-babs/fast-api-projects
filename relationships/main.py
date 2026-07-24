from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from database import engine, get_db

app = FastAPI()

@app.get("/")
def home():
    return "I'm am learning about database relationships."




