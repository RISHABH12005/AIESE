# =========================================================
# Intelligence Layer
# =========================================================

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