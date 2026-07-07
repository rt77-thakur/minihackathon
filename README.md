# Quiz Generator with LangChain + Groq

A simple Python script that generates multiple‑choice quiz questions using **LangChain** and **Groq's LLM**.  
You can specify the topic, number of questions, and difficulty level (easy, medium, hard).

---

## 🚀 Features
- Generate quiz questions on any topic
- Choose difficulty level: easy, medium, or hard
- Each question has 4 options with the correct answer marked
- Uses `.env` file to securely load your Groq API key

---

## 📦 Requirements
- Python 3.9+
- Packages:
  - `python-dotenv`
  - `langchain-groq`
  - `langchain-core`

Install dependencies:
```bash
pip install python-dotenv langchain-groq langchain-core
