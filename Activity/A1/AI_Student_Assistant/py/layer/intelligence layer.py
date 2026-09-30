import streamlit as st

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
	if query.strip():
		intent = identify_intent(query)
		st.write("Your question:", query)
		st.write("Identified Intent:", intent)
	else:
		st.warning("Please enter a question.")
