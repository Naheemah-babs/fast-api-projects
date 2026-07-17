from fastapi import FastAPI, Response
from pydantic import BaseModel, Field

app = FastAPI()

class Student(BaseModel):
    name: str = Field(
        min_length = 3,
        max_length = 8,
        default = "Carrie"
    )
    email: str
    year_of_birth: int = Field(
        ge = 2005,
        le = 2025
    )
    age: int | None = None

@app.post("/student")
def create_student(student: Student):
    cal_age = 2025 - student.year_of_birth
    student.age = cal_age

    return{
        "message": "student created",
        "student": student
    }