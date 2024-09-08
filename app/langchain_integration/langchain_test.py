from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

def create_llm_instance():
    llm = ChatGroq(
        model="llama-3.1-70b-versatile",
        temperature=0,
        groq_api_key= os.getenv('GROQ_API_KEY')
        # other params...
    )
    return llm

llm_instance = create_llm_instance()
# response = llm_instance.invoke("What is machine learning?")

# print(response.content)

