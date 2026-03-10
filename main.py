import os
from dotenv import load_dotenv

# 1. Load the vault FIRST
load_dotenv()

# 2. THEN import the agents (now they can see the key)
from crewai import Crew, Process
from agent import researcher, writer
from task import research_task, writing_task

# ... rest of your code ...

# 1. Load API Keys safely from the .env file
load_dotenv()

# 2. Assemble the Crew
# We use a sequential process so the researcher finishes before the writer starts
content_squad = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    verbose=True # This lets you see the "thinking" process in the terminal
)

# 3. Kickoff the Workflow
# Wrap everything in a function so app.py can call it
def run_crew(youtube_url):
    inputs = {
        'youtube_url': youtube_url
    }
    # content_squad is your Crew object
    result = content_squad.kickoff(inputs=inputs)
    return result

# Keep this so you can still run it via terminal if you want
if __name__ == "__main__":
    url = "YOUR_TEST_URL"
    print(run_crew(url))