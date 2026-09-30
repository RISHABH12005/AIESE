import json
from pathlib import Path

courses_file = Path(__file__).resolve().parent.parent / "json" / "courses.json"

with courses_file.open("r", encoding="utf-8") as file:
	courses = json.load(file)
