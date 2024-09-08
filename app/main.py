from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import uuid
from prompt_util.prompt_util import generate_prompt
from cronmaDb.cromaDb_setup import initialize_clients
from utils.write_email_prompt import write_mail
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize clients and get the persistent client
_, chroma_persistent_client = initialize_clients()
        

def get_query_links(collection, skills):
    return collection.query(query_texts=skills, n_results=2).get('metadatas', [])

@app.route('/generate-email', methods=['POST'])
def generate_email():
    try:
        # Get input data from the frontend (JSON format)
        data = request.get_json()
        username = data.get("username", "Ali")  # Default to 'Ali' if not provided
        
        # Read CSV file into DataFrame
        # df = pd.read_csv("my_portfolio.csv")
        
      
        # Get or create the collection
        collection = chroma_persistent_client.get_or_create_collection(name="portfolio")
        
        # Add documents to the collection
        # for _, row in df.iterrows():
        #     techstack = row.get("Techstack", "")
        #     links = row.get("Links", "")
        #     if techstack:
        #         collection.add(
        #             documents=[techstack],
        #             metadatas={"links": links},
        #             ids=[str(uuid.uuid4())]
        #         )
        #     else:
        #         logging.warning("Skipping row with empty 'Techstack': %s", row)
        
        # Generate job data
        jobs = generate_prompt()
        
        # For each job, query links and generate the email
        emails = []
        for job in jobs:
            skills = job.get('skills', [])
            links = get_query_links(collection=collection, skills=skills)
            email = write_mail(job=job, links=links, username=username)
            emails.append(email)
        
        # Return the generated emails as a JSON response
        return jsonify({"emails": emails}), 200
    
    except Exception as e:
        logging.error("An error occurred: %s", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
