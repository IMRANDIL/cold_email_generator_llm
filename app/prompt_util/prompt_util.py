# prompt_generator.py

from langchain_core.prompts import PromptTemplate
from web_scrapping.web_scrapp import scrape_page
from langchain_integration.langchain_test import create_llm_instance
from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import JsonOutputParser



import re

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]*?>', '', text)
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s{2,}', ' ', text)
    # Trim leading and trailing whitespace
    text = text.strip()
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text



def generate_prompt():
    # Get the scraped data
    page_data = clean_text(scrape_page())

    # Define the prompt template
    prompt_extract = PromptTemplate.from_template(
        """
        ### INPUT TEXT:
        {page_data}
        ### TASK:
        Extract the job postings from the given text and return a valid JSON object with the following keys: 
        `role`, `experience`, `skills`, and `description`. Ensure the JSON is properly formatted and contains only the required fields.

        ### OUTPUT:
        Return only the JSON object without any additional text or explanation.
        """
    )
    
    llm = create_llm_instance()
    
    chain_extract = prompt_extract | llm

    # Substitute the page data into the prompt template
    prompt_with_data = chain_extract.invoke(input={'page_data': page_data})

    # Parsing the result and ensuring it's returned as a list
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(prompt_with_data.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    
    # Return as a list or wrap in a list if it's a single item
    return res if isinstance(res, list) else [res]

