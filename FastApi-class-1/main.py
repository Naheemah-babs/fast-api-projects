from fastapi import FastAPI, Response

app = FastAPI()


# creating a route
@app.get("/")
def main():
    return {"message": "Hello FastAPI"}

# creating about route

@app.get("/about")
def about():
    return {"message": "First class on FastApi"}

@app.get("/student")
def student():
    names = {"tom", "brady", "sam"}
    return {
        "students": names
    }

@app.get("/student/{students_id}")
def student(students_id: int):
    names = ["tom", "brady", "sam"]
    try:
        student_name = names[students_id]
        return {
            "students": student_name,
            "serial_id": students_id
        }
    except:
        return Response ("user not found", status_code=404)
