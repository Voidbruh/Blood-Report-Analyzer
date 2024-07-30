from crewai import Task

# Creating tasks for the agents
class Tasks:
    def __init__(self):
        pass

    def analyze_report(self, agent, text):
        return Task(
            description=f"""
                Analyze the provided blood report text and provide a summary to the user.

                - The report contains various categories related to blood with defined values.
                - Determine if each category's value is within the normal range.
                - If the normal range is provided, compare the value to it; otherwise, search the internet to determine if the value is normal for a human. Don't keep searching repeatedly; if you don't get it after searching a few times, leave it.
                - Summarize the report, indicating which categories are normal and which are abnormal.
                - Use the provided text directly for analysis.
                - Use the Units given and the Bio. Ref. Interval for normal ranges.
            """,
            agent=agent,
            expected_output="Summarized Blood Report",
            async_execution=False,
            inputs={"text": text}
        )

    def recommend_articles(self, agent, text):
        return Task(
            description=f"""
                Revise the summary provided, focusing on abnormal values.

                - Search the internet for articles regarding detected abnormalities and health recommendations to address them. Don't keep searching repeatedly; if you don't get it after searching a few times, leave it.
                - Return links to articles discussing the detected abnormalities, health recommendations, and links of supporting articles.
                - Use the provided text directly for analysis.
                - Use the Units given and the Bio. Ref. Interval for normal ranges.
            """,
            agent=agent,
            expected_output="List of Health Recommendations and Supporting Articles Links",
            async_execution=False,
            inputs={"text": text}
        )
