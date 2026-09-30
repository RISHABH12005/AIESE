import json
import os
from pathlib import Path

from google import genai

def run_inference(query, courses):
	api_key = os.getenv("GEMINI_API_KEY")
	if not api_key:
		raise RuntimeError("GEMINI_API_KEY is not set in this PowerShell session.")

	client = genai.Client(api_key=api_key)
	knowledge = json.dumps(courses, indent=2)
	prompt = f"""
You are a university course recommendation assistant.

Student query:
{query}

Available course information:
{knowledge}

Recommend the most suitable course based only on:
1. The student's query
2. The available course information

Do not invent any course or prerequisite.

Give the response in this format:
Recommended Course:
Reason:
Prerequisite:
Credits:
"""

	interaction = client.interactions.create(
		model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
		input=prompt,
	)
	return interaction.output_text

if __name__ == "__main__":
	courses_file = Path(__file__).resolve().parent.parent / "json" / "courses.json"
	with courses_file.open("r", encoding="utf-8") as file:
		courses = json.load(file)

	print(run_inference("I want to learn machine learning", courses))
