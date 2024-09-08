# AI-Powered Job Extraction and Cold Email Generator

This project leverages cutting-edge AI tools and frameworks to automate the process of extracting job postings from web pages, and generating personalized cold emails for job applications based on user input and a customizable portfolio of skills. It integrates Groq-powered LLM (Language Learning Model), Langchain prompts, web scraping, and vector databases to streamline the end-to-end process of job application creation.

## Features

- **Web Scraping:** Automatically extracts job postings from dynamic web pages using `WebBaseLoader` and cleans the extracted data to eliminate noise.
- **Job Posting Extraction:** Utilizes Langchain's LLM prompt chains to extract and format relevant job details (role, experience, skills, description) into valid JSON objects.
- **Personalized Cold Emails:** Generates tailored cold emails using a Groq-powered LLM, customizable with the candidate's skills and relevant portfolio links.
- **Vector Database Integration:** Stores tech stack and portfolio metadata using Chromadb for efficient querying of relevant links for the cold email.
- **Dynamic Email Generation:** Creates personalized, results-driven emails that align with job descriptions and highlight the most relevant experience and projects.
  
## Technologies Used

- **LLM Integration (Groq):** ChatGroq (Llama-3.1-70B) model for high-accuracy text generation.
- **Langchain:** Used for creating dynamic prompt templates and chaining LLMs to generate responses.
- **Flask:** Backend server to handle email generation requests and manage job scraping and LLM interaction.
- **React.js:** Frontend for collecting user input (e.g., username) and triggering the email generation process.
- **Chromadb:** Vector database for efficient metadata storage and querying.
- **Pandas:** Used for handling portfolio CSV data and processing it for storage in Chromadb.
- **Flask-CORS:** Enabling CORS for the Flask backend.

## Setup Instructions

### Prerequisites

- Python 3
- Node.js and npm (for React frontend)
- Groq API key (for LLM integration)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/IMRANDIL/cold_email_generator_llm.git
   cd cold_email_generator_llm
   ```

2. **Backend Setup (Flask):**
   - Create and activate a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install the required Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Set up environment variables for the Groq API key:
     ```bash
     export GROQ_API_KEY="your-api-key"
     ```
   - Start the Flask server:
     ```bash
     python app.py
     ```

3. **Frontend Setup (React):**
   - Navigate to the `frontend` directory:
     ```bash
     cd frontend
     ```
   - Install the dependencies:
     ```bash
     npm install
     ```
   - Start the React development server:
     ```bash
     npm run dev
     ```

### Usage

- Visit the frontend interface to input the username and trigger the email generation process.
- The backend will scrape job postings, process them with Langchain prompts, query the vector database, and generate customized cold emails for each job.
- Emails are returned in JSON format and are displayed in a well-formatted code block with a "Copy to Clipboard" feature.

### Example Output

```json
{
  "subject": "Application for Lead Software Engineer at XYZ Inc.",
  "body": "Dear Hiring Manager, I am writing to express my interest in the Lead Software Engineer position..."
}
```

## Future Enhancements

- **Dynamic Web Scraping:** Extend web scraping capabilities to handle more complex and dynamic job posting websites.
- **Advanced Querying:** Improve the vector database querying mechanism to handle multiple skill sets more efficiently.
- **UI Enhancements:** Further enhance the React.js frontend for better user experience and support for multiple email templates.
- **Multiple API Integration:** Explore integration with other LLM models (OpenAI, etc.) for increased versatility.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
