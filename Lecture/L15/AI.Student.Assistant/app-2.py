import streamlit as st

st.title("AI Student Assistant")

# Intelligence Layer
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


# Client Layer
query = st.text_input("Ask your question")

if st.button("Submit"):
    intent = identify_intent(query)

    st.write("Your question:")
    st.write(query)

    st.write("Identified Intent:")
    st.write(intent)