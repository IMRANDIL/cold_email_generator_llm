from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    groq_api_key='gsk_**********'
    # other params...
)

response = llm.invoke("What is machine learning?")

# print(response.content)

