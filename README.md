# CrewAI Blood Report Analyzer

## Description

This Project uses the CrewAI framework to create a crew of agents to Analyze Blood Test Reports. The crew takes as input the pdf file of the bllod test report, analyzes it and finds out the normal and abnormal values using the reference ranges(reference ranges are searched online if not provided), summarizes the values with normal and abnormal values, then searches the internet for articles tailored to the person's health needs based on the blood test results, and finally provides health recommendations along with relevant article links.

## Code Description

This project contains 2 agents specialized for different tasks:

### Blood Report Summarization Expert

- **Role**: Expert Blood Analyser and Report Summarizer
- **Backstory**: Expert in blood report analysis. Provides comprehensive reports on blood tests. Determines whether blood values are within normal ranges and provides a comprehensive summary of the blood categories with their values and if they are normal or abnormal.
- **Goal**: Summarize the blood report, identifying normal and abnormal values. Provide health recommendations and links to articles for each abnormality found.

### Health Recommender Expert

- **Role**: Expert in Providing Health Recommendations
- **Backstory**: Expert in providing Health Recommendations and relevant articles. Finds out the relevant articles and the ecommendation from online about the abnormal values and gives well tailored health recommendation based on the blood report values.
- **Goal**: Summarizes the normal and abnormal values in the report then gives well tailored recommendations along with article links.


## Key Features

1. **Framework**: Utilize the CrewAI framework.
2. **Data Input**:  Takes the PDF file of the blood test report as Input.
3. **Data Analysis**: Analyze the blood test report to extract relevant health information.
4. **Web Search**: Implement web search functionality to search the internet for articles related to the person's health needs.
5. **Recommendations**: Generate health recommendations based on the analyzed data and the retrieved articles.


## Approach

1.  Setting up the environment by installing relevant libraries and setting up necessary environment variables for the API keys.
2.  Initialised tools required by the agents for reading PDF files and SerperDevTool for searching the web.
3.  Defined the 2 Agents and gave them the corresponding role, goal and backstory. The Agents used were Blood Report Summarization Expert and Health Recommender Expert.
4.  Used the **mixtral-8x7b-32768**, after testing out different models for the same task. Some of other different models that were tried are -  
llama-3.1-8b-instant, llama3-70b-8192, gemma-7b-it, gemma2-9b-it.  
> **Note:** llama 3.1 8b couldn't be used because of the rate limits as it's only on preview at the moment. llama3-70b model showed great potential but didn't get satisfying results due to the time constraint.
6.  Defined the 2 Tasks to be done by the agents and created a detailed description for both tasks. These tasks take the text directly as inputs when initialised.
7.  Used the pdfplumber library to extract the tables from the pdf and convert them to text form then feed that to the tasks.
8.  Finally, I kicked off the crew's process to execute the task.


## Usage

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Voidbruh/Blood-Report-Analyzer.git
    cd Blood-Report-Analyzer
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your API keys:**

    Replace the placeholders in the script with your actual API keys for Serper, Groq and OpenAI.

    ```python
    os.environ["SERPER_API_KEY"] = "YOUR API KEY"
    os.environ["GROQ_API_KEY"] = "YOUR API KEY"
    os.environ["OPENAI_API_KEY"] = "YOUR API KEY (WRITE NA IF YOU DON'T INTEND TO USE OPENAI API)"
    ```

### Execution

- Place the Blood Test Report in the directory specified.
- Execute the main script of crew.py.
    ```bash
    python crew.py
    ```
- When Prompted, Enter the PDF File name that's present in the directory.
