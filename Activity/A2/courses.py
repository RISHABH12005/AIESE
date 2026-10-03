from fastapi import FastAPI, HTTPException

app = FastAPI()

courses = [
    {
        "id": 1,
        "name": "Artificial Intelligence",
        "category": "AI"
    },
    {
        "id": 2,
        "name": "Cyber Security",
        "category": "Cyber Security"
    },
    {
        "id": 3,
        "name": "Data Science",
        "category": "Data Science"
    },
    {
        "id": 4,
        "name": "Machine Learning",
        "category": "AI"
    }
]


@app.get("/")
def home():
    return {"message": "Welcome to Course Service"}


@app.get("/courses")
def get_courses():
    return courses


@app.get("/courses/{course_id}")
def get_course(course_id: int):

    for course in courses:
        if course["id"] == course_id:
            return course

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )