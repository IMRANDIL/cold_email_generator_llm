# LangChain Integration and CromaDB Test Project
This project is a collection of tests and integrations for LangChain and CromaDB. It aims to demonstrate the capabilities of these technologies in processing and managing natural language data.

## LangChain Integration
The LangChain integration test, located in `app/langchain_integration/langchain_test.py`, showcases the use of the LangChain API for processing natural language queries. It leverages the ChatGroq model to generate responses to user queries, such as "What is machine learning?".

## CromaDB Test
The CromaDB test, located in `app/cronmaDb/cromaDb_test.py`, demonstrates the creation and management of a document collection using the CromaDB client. It adds documents to a collection, retrieves them, and prints the results.

## Configuration
The project includes a configuration file, `config.txt`, which contains the API key for LangChain. This file is ignored by the version control system to prevent sensitive information from being committed.

## Ignored Files
The project's `.gitignore` file specifies directories and files that should be ignored by the version control system. These include the virtual environment directory, configuration files, and environment variables.

## Getting Started
To run the tests and integrations in this project, ensure you have the necessary dependencies installed. You can do this by running `pip install -r requirements.txt` in your terminal. Then, execute the test files using Python, for example, `python app/langchain_integration/langchain_test.py`.

## Contributing
Contributions to this project are welcome. If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.
