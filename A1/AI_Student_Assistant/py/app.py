import os
import json

from dotenv import load_dotenv
import streamlit as st

from openai import OpenAI
from google import genai

from knowledge_layer import courses
from intelligence_layer import identify_intent
from tools_layer import register_course, get_registrations

# Load Environment Variables
load_dotenv()

# =========================================================
# OpenAI Client
# =========================================================

openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


# =========================================================
# Gemini Client
# =========================================================

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# =========================================================
# OpenAI Inferencing Layer
# =========================================================

def run_openai_inference(query, courses):

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

    response = openai_client.responses.create(
        model=os.getenv(
            "OPENAI_MODEL",
            "gpt-4o-mini"
        ),
        input=prompt
    )

    return response.output_text


# =========================================================
# Gemini Inferencing Layer
# =========================================================

def run_gemini_inference(query, courses):

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

    interaction = gemini_client.interactions.create(
        model=os.getenv(
            "GEMINI_MODEL",
            "gemini-3.8-flash"
        ),
        input=prompt
    )

    return interaction.output_text


# =========================================================
# Client Layer
# =========================================================

st.title("AI Student Assistant")

student_name = st.text_input("Enter your name")

query = st.text_input("Ask your question")


# =========================================================
# AI Provider
# =========================================================

provider = st.selectbox(
    "Select AI Provider",
    ["OpenAI", "Gemini"]
)


# =========================================================
# Submit
# =========================================================

if st.button("Submit"):

    # -----------------------------------------------------
    # Intelligence Layer
    # -----------------------------------------------------

    intent = identify_intent(query)

    st.write("Identified Intent:")

    st.write(intent)


    # -----------------------------------------------------
    # Inferencing Layer
    # -----------------------------------------------------

    if intent == "course_recommendation":

        if provider == "OpenAI":

            result = run_openai_inference(
                query,
                courses
            )

        else:

            result = run_gemini_inference(
                query,
                courses
            )

        st.subheader("AI Recommendation")

        st.write(result)

    else:

        st.info(
            "Currently, this application supports "
            "course recommendation queries."
        )


# =========================================================
# Tools Layer — Register Recommended Course
# =========================================================

if st.button("Register Recommended Course"):

    if student_name:

        message = register_course(
            student_name,
            "Artificial Intelligence"
        )

        st.success(message)

    else:

        st.warning("Please enter your name first.")


# =========================================================
# Tools Layer — Show Registrations
# =========================================================

if st.button("Show Registrations"):

    registrations = get_registrations()

    st.subheader("Registered Students")

    if registrations:

        for registration in registrations:

            st.write(registration)

    else:

        st.info("No registrations found.")