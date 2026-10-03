from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Request data ka format
class StudentRequest(BaseModel):
    name: str
    interest: str


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Intelligent Recommendation API"
    }


# Intelligent API endpoint
@app.post("/recommend")
def recommend(student: StudentRequest):

    interest = student.interest.lower()

    # Rule-based intelligent decision
    if "ai" in interest or "artificial intelligence" in interest:
        recommendation = "Artificial Intelligence"

    elif "cyber" in interest or "security" in interest:
        recommendation = "Cyber Security"

    elif "data" in interest or "analytics" in interest:
        recommendation = "Data Science"

    elif "machine learning" in interest or "ml" in interest:
        recommendation = "Machine Learning"

    else:
        recommendation = "No suitable course found"

    return {
        "student_name": student.name,
        "interest": student.interest,
        "recommendation": recommendation
    }