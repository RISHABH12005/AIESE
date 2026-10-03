from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

STUDENT_SERVICE = "http://127.0.0.1:8000"
COURSE_SERVICE = "http://127.0.0.1:8001"


class RecommendationRequest(BaseModel):
    student_id: int


@app.get("/")
def home():
    return {"message": "Welcome to Recommendation Service"}


@app.post("/recommend")
def recommend(request: RecommendationRequest):

    # 1. Get student information
    student_response = requests.get(
        f"{STUDENT_SERVICE}/students/{request.student_id}"
    )

    if student_response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student = student_response.json()

    # 2. Get course information
    course_response = requests.get(
        f"{COURSE_SERVICE}/courses"
    )

    if course_response.status_code != 200:
        raise HTTPException(
            status_code=503,
            detail="Course Service unavailable"
        )

    courses = course_response.json()

    # 3. Get student interests
    interests = [
        interest.lower()
        for interest in student["interests"]
    ]

    # 4. Find matching courses
    recommendations = []

    for course in courses:

        course_name = course["name"].lower()
        category = course["category"].lower()

        for interest in interests:

            if interest in course_name or interest in category:
                recommendations.append(course)
                break

    # 5. Return recommendation
    return {
        "student": student["name"],
        "interests": student["interests"],
        "recommendations": recommendations
    }