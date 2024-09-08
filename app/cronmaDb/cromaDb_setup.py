import chromadb

def initialize_clients():
    # Initialize the clients
    chroma_client = chromadb.Client()
    chroma_persistent_client = chromadb.PersistentClient('vectorStore')
    
    # # Create a collection in the temporary client
    # collection = chroma_client.create_collection(name="my_collection")
    
    # # Add documents to the collection
    # collection.add(
    #     documents=[
    #         "India is a country located in South Asia, known for its diverse culture and rich history.",
    #         "Egypt is a country located in northeastern Africa, famous for its ancient pyramids and the Nile River."
    #     ],
    #     ids=['id01', 'id02']
    # )
    
    # # Retrieve all documents
    # all_doc = collection.get()
    
    # # Query the collection
    # result = collection.query(
    #     query_texts=["Query is about Cairo"],
    #     n_results=2
    # )
    
    # print(result)
    
    return chroma_client, chroma_persistent_client

# Example usage
chroma_client, chroma_persistent_client = initialize_clients()
