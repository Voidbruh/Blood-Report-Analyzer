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


