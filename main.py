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
if __name__ == "__main__":
    print("🚀 Launching the Agentic Content Squad...")
    
    # You can change this URL to any video you want to analyze
    inputs = {'youtube_url': 'https://youtu.be/Qa_4c9zrxf0?si=Utw-fCuY3vUBe6Vu'}
    
    result = content_squad.kickoff(inputs=inputs)

    # 4. Save the Final Output to a file for your portfolio
    print("\n\n########################")
    print("## FINAL CONTENT GENERATED ##")
    print("########################\n")
    print(result)
    
    with open('output/vs_code_output.md', 'w') as f:
        f.write(str(result))