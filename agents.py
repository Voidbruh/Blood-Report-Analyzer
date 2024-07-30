from crewai import Agent
import os
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool, WebsiteSearchTool

# Instantiate the language model
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="mixtral-8x7b-32768",
)

# Instantiate the tools
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

# Define the Agents class
class Agents:
    def __init__(self):
        pass

    def report_summarizer(self):
        return Agent(
            role="Blood Report Summarization Expert",
            goal="""
                Summarize the blood report provided by finding all normal and abnormal values from the blood report.

                You are given a blood report of a person with different categories of blood along with their values.
                If you don't understand a category, search it online and understand it. Also, check if every category
                value falls within its reference range. If the range is given in the report itself, use it; else search
                online to find the range of values. Don't keep searching repeatedly; if you don't get it after searching a
                few times, leave it.

                Finally, you are supposed to create a summarized report that must mention all the values and categories that
                are normal and all those that are abnormal.
                """,
            backstory="""
                    You are an expert Blood Report Summarizer. Your job includes providing comprehensive information
                    about a person's blood from their blood report information. You should cover the normal and abnormal
                    values detected in their blood. You should output all the relevant details which would be useful for
                    understanding the person's blood report. If you don't understand or know something in the report, you
                    will search it online and get the correct information.
                    """,
            tools=[
                search_tool,
                web_rag_tool
            ],
            verbose=True,
            memory=True,
            llm=llm
        )
    
    def health_recommender(self):
        return Agent(
            role="Health Recommender Expert",
            goal="""
                Your goal is to get a detailed summary of both the normal and abnormal values found in the blood report. This 
                summary should include well-tailored health recommendations based on the blood report to address any abnormalities
                detected. You should also include links to articles providing further information and insights. Don't keep searching 
                repeatedly; if you don't get it after searching a few times, leave it.
                """,
            backstory="""
                    You are an expert Health Recommender who understands blood report information and can find out the normal and abnormal
                    values. You know all about the different types of blood measurements and which ranges they should fall between.
                    You will find out the ranges online if they aren't specified in the report itself. You will also find relevant
                    article links from online.
                    """,
            tools=[
                search_tool,
                web_rag_tool
            ],
            verbose=True,
            memory=True,
            llm=llm
        )
