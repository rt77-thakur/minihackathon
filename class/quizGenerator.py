from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(model_name="llama-3.3-70b-versatile")

template = """
Generate {number} multiple-choice questions on {topic}.
Each question should have 4 options and mark the correct one clearly.
Format:
Question: <text>
Options: A) ... B) ... C) ... D) ...
Answer: <correct option>
"""
prompt = PromptTemplate.from_template(template)
chain = prompt | llm

userInput= input("Enter the Topic for Quiz: ")
userNumber = int(input("Enter the Number of Questions: "))


print(chain.invoke({"number":userNumber,"topic":userInput}).content)
