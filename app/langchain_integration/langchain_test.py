from langchain_groq import ChatGroq

def create_llm_instance():
    llm = ChatGroq(
        model="llama-3.1-70b-versatile",
        temperature=0,
        groq_api_key='gsk_a**********************************'
        # other params...
    )
    return llm

llm_instance = create_llm_instance()
# response = llm_instance.invoke("What is machine learning?")

# print(response.content)

