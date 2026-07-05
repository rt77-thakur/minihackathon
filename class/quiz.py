import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Load API keys
load_dotenv()

# Backend connection
llm = ChatGroq(model_name="llama-3.3-70b-versatile")

template = """
Generate 3 multiple-choice questions on {topic}.
Each question should have 4 options and mark the correct one.
"""
prompt = PromptTemplate.from_template(template)
chain = prompt | llm

# --- Frontend ---
st.title("LangChain Quiz Generator 🎮")

topic = st.text_input("Enter a topic for your quiz:")
if topic:
    result = chain.invoke({"topic": topic}).content
    
    # Split into lines
    lines = result.strip().split("\n")
    
    # Display quiz interactively
    current_question = ""
    options = []
    for line in lines:
        if line.strip() == "":
            continue
        if line[0].isdigit():  # new question
            if current_question:
                st.write(current_question)
                st.radio("Choose an answer:", options, key=current_question)
            current_question = line
            options = []
        elif line.strip().startswith(("A", "B", "C", "D")):
            options.append(line)
        else:
            current_question += " " + line
    
    # Show last question
    if current_question:
        st.write(current_question)
        st.radio("Choose an answer:", options, key=current_question)
