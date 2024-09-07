# from langchain_community.document_loaders import WebBaseLoader

# # loader_multiple_pages = WebBaseLoader(["https://www.espn.com/", "https://google.com"])

# # docs = loader.load()

# # docs[0]

# loader = WebBaseLoader("https://jobs.nike.com/job/R-36827")

# page_data = loader.load().pop().page_content

# # print(page_data)


# web_scrapp.py

from langchain_community.document_loaders import WebBaseLoader

def scrape_page():
    loader = WebBaseLoader("https://jobs.nike.com/job/R-36827")
    page_data = loader.load().pop().page_content
    return page_data
