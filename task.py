from crewai import Task
from agent import researcher, writer

# 1. Update the Research Task to command tool usage
research_task = Task(
    description=(
        "1. MUST USE the 'YouTube Transcript Scraper' tool to extract the exact transcript from this URL: {youtube_url}\n"
        "2. Read the resulting transcript text to identify the 'Big Idea'.\n"
        "3. Extract 3 high-energy 'hooks' actually spoken in the video.\n"
        "4. Summarize the top 5 key takeaways that provide the most value."
    ),
    expected_output="A structured report containing the Big Idea, 3 viral hooks, and 5 key takeaways in Markdown format.",
    agent=researcher
)

# 2. The Writing Task stays exactly the same
writing_task = Task(
    description=(
        "1. Use the specific insights from the Research Task.\n"
        "2. Draft 5 professional LinkedIn posts focusing on industry lessons.\n"
        "3. Draft 2 X (Twitter) threads (5 tweets each) using a 'Hook -> Value -> CTA' structure.\n"
        "4. Ensure the tone is 'Helpful Peer' and avoids all AI clichés."
    ),
    expected_output=(
        "A comprehensive document containing all 5 LinkedIn posts "
        "and both X threads, formatted for immediate posting."
    ),
    agent=writer,
    context=[research_task] # Forces the writer to wait for the researcher's scraped data
)