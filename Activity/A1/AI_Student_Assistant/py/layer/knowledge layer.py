
import json
from pathlib import Path

import streamlit as st

courses_file = Path(__file__).resolve().parent.parent / "json" / "courses.json"

with courses_file.open("r", encoding="utf-8") as file:
	courses = json.load(file)

def identify_intent(query):
	query = query.lower()

	if "course" in query or "learn" in query:
		return "course_recommendation"
	elif "fee" in query or "payment" in query:
		return "fee_information"
	elif "placement" in query or "job" in query:
		return "career_guidance"
	else:
		return "general_query"

st.title("AI Student Assistant")
query = st.text_input("Ask your question")

if st.button("Submit"):
	intent = identify_intent(query)
	st.write("Identified Intent:", intent)

	if intent == "course_recommendation":
		st.write("Available Course Information:")

		for course in courses:
			st.write("Course:", course["course"])
			st.write("Prerequisite:", course["prerequisite"])
			st.write("Credits:", course["credits"])
			st.write("Description:", course["description"])
			st.write("---")
