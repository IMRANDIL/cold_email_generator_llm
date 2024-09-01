import chromadb
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=[
        "India is a country located in South Asia, known for its diverse culture and rich history.",
        "Egypt is a country located in northeastern Africa, famous for its ancient pyramids and the Nile River."
    ],
    ids = ['id01', 'id02']
)

all_doc = collection.get()
print(all_doc)