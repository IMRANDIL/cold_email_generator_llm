import pandas as pd
import uuid
from prompt_util.prompt_util import generate_prompt
from cronmaDb.cromaDb_setup import initialize_clients
from utils.write_email_prompt import write_mail
import logging


# Set up logging
logging.basicConfig(level=logging.INFO)

def get_query_links(collection, skills):
    return collection.query(query_texts=skills, n_results=2).get('metadatas', [])

def main():
    try:
        # Read CSV file into DataFrame
        df = pd.read_csv("my_portfolio.csv")
        
        # Initialize clients and get the persistent client
        _, chroma_persistent_client = initialize_clients()
        
        # Get or create the collection
        collection = chroma_persistent_client.get_or_create_collection(name="portfolio")
        
        # Add documents to the collection
        for _, row in df.iterrows():
            # Ensure 'Techstack' and 'Links' columns exist in the DataFrame
            techstack = row.get("Techstack", "")
            links = row.get("Links", "")
            if techstack:  # Add only if 'Techstack' is not empty
                collection.add(
                    documents=[techstack],
                    metadatas={"links": links},
                    ids=[str(uuid.uuid4())]  # Generate a unique ID for each document
                )
            else:
                logging.warning("Skipping row with empty 'Techstack': %s", row)

        # Output DataFrame and parsed result
        jobs = generate_prompt()
        # print(result)
        # json_parser = JsonOutputParser()
        # jobs = json_parser.parse(result)
        for job in jobs:
                skills = job.get('skills', [])
                links = get_query_links(collection=collection, skills=skills)
                email = write_mail(job=job, links=links, username='Ali')
                print(email)
        
    except Exception as e:
        logging.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()
