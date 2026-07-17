from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class Student(BaseModel):
    name: str = Field(
        min_length = 3,
        max_length = 8,
        default = "Carrie"
    )
    email: EmailStr
    year_of_birth: int = Field(
        ge = 2005,
        le = 2025
    )
    age: int | None = None

@app.post("/student", status_code = status.HTTP_201_CREATED)
def create_student(student: Student):
    cal_age = 2025 - student.year_of_birth
    student.age = cal_age
    database = ["ade@ade.com", "ola@ola.com", "jide@jide.com"]

    if student.email in database:
        raise HTTPException(
            detail = "Email already exists",
            status_code = status.HTTP_409_CONFLICT
        )

    return{
        "message": "student created",
        "student": student
    }