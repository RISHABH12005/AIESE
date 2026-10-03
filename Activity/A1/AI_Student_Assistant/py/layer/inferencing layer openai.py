import json
import os

from openai import OpenAI

client = OpenAI()

def run_inference(query, courses):
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
	response = client.responses.create(
		model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
		input=prompt,
	)
	return response.output_text
