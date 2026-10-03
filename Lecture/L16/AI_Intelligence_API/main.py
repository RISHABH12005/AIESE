from fastapi import FastAPI, HTTPException
app = FastAPI()
# Home Endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Course API"
    }
# Courses Data
cources =[
    {
        "id": 1,
        "name": "Artificial Intelligence"
    },
    {
        "id": 2,
        "name": "Cyber Security"
    },
        {
        "id": 3,
        "name": "Data Science"
    }
]
# Courses Endpoint
@app.get("/courses")
def get_courses():
    return  cources
@app.get("/courses/{course_id}")
def get_course(course_id: int):
    for course in cources:
        if course["id"] == course_id:
            return course
        raise HTTPException(status_code=404, detail="Course not found")
    