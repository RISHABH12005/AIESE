
from fastapi import FastAPI, HTTPException

app = FastAPI()

students = [
    {
        "id": 101,
        "name": "Rahul",
        "interests": ["AI", "Cyber Security"]
    },
    {
        "id": 102,
        "name": "Priya",
        "interests": ["Data Science"]
    },
    {
        "id": 103,
        "name": "Aman",
        "interests": ["Cyber Security"]
    }
]


@app.get("/")
def home():
    return {"message": "Welcome to Student Service"}


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )