# prompt_generator.py

from langchain_core.prompts import PromptTemplate
from web_scrapping.web_scrapp import scrape_page
from langchain_integration.langchain_test import create_llm_instance

def generate_prompt():
    # Get the scraped data
    page_data = scrape_page()

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

    return prompt_with_data.content
