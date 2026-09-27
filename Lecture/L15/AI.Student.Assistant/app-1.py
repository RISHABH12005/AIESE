import streamlit as st
st.title("AI Student Assistant")
query = st.text_input("Ask your question")
if st.button("Submit"):
    st.write(query)
    
