from langchain_core.prompts import PromptTemplate
from langchain_integration.langchain_test import create_llm_instance

def write_mail(job, links, username):
    prompt_email = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}

        ### INSTRUCTION:
        You are {username}, a skilled Software Engineer with a proven track record of empowering enterprises by delivering 
        tailored solutions that enhance scalability, optimize processes, reduce costs, and improve overall efficiency. 

        Write a compelling cold email to the client regarding the job description provided, highlighting how your experience 
        and skills can meet their needs. Include the most relevant links from the following list to showcase your expertise:
        {link_list}

        Do not provide any preamble or irrelevant information. Remember, you are {username}, a Software Engineer focused 
        on results and client satisfaction.

        ### EMAIL (NO PREAMBLE, NO EXTRA NEWLINES AFTER "complimentary close"):
        """
    )
    llm = create_llm_instance()
    chain_email = prompt_email | llm
    res = chain_email.invoke({"job_description": str(job), "link_list": links, "username": username})
    return res.content
