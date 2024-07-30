from crewai import Crew, Process
from agents import Agents
from tasks import Tasks
from textconvertor import tables_from_pdf, table_to_text
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Instantiate agents
agents = Agents()
report_summarizer = agents.report_summarizer()
health_recommender = agents.health_recommender()

# Enter your File name as input (ex- Patient Report.pdf)
# Note - Have the file in the directory
report_path = input("Enter Your PDF File Name")

# Extract tables from PDF
tables = tables_from_pdf(report_path)

if tables:
    text = table_to_text(tables)
    logging.info("Successfully extracted text from PDF")
else:
    logging.error('Failed to extract tables')
    text = ""  # Ensure text is defined

# Instantiate tasks
tasks = Tasks()
analyze_report = tasks.analyze_report(report_summarizer, text)
recommend_articles = tasks.recommend_articles(health_recommender, text)

# Create the crew
crew = Crew(
    agents=[report_summarizer, health_recommender],
    tasks=[analyze_report, recommend_articles],
    process=Process.sequential,
    verbose=True
)

# Define the inputs
inputs = {
    'text': text
}

# Kick off the crew
try:
    crew.kickoff(inputs)
except Exception as e:
    logging.error(f"Error during crew kickoff: {e}")
