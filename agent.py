import os
from crewai import Agent, LLM
from tools import YouTubeScraperTool 

# Initialize your custom bulletproof tool
scraper_tool = YouTubeScraperTool()

# THE LOCAL BRAIN: Using the smarter 3B model entirely on your hardware
local_llm = LLM(
    model="ollama/llama3.2", 
    base_url="http://localhost:11434",
    timeout=1200 # Gives your GPU 20 minutes before it forces a crash
)

# The dummy key to bypass CrewAI's internal cloud checks
os.environ["OPENAI_API_KEY"] = "NA"

# Researcher Agent (Local)
# ... (LLM और Tool वाला ऊपर का कोड वैसा ही रहेगा) ...

# Researcher Agent Update
researcher = Agent(
    role='Lead Video Researcher',
    goal='Extract high-energy hooks and key business insights from {youtube_url}',
    backstory=(
        "You are a meticulous data extractor. Your ONLY job is to provide a detailed "
        "summary of the video transcript. Do not use conversational filler. Just provide "
        "the facts and insights clearly for the writer to use."
    ),
    allow_delegation=False,
    verbose=True,
    tools=[scraper_tool], 
    llm=local_llm,
    memory=False
)

# Writer Agent Update (The Fix for your specific error)
writer = Agent(
    role='Social Media Architect',
    goal='Draft 5 LinkedIn posts and 2 Twitter threads based on research',
    backstory=(
        "You are a world-class copywriter. You will be provided with research notes. "
        "You MUST NOT ask for more information. You MUST NOT say 'I need more notes.' "
        "Take whatever text you receive and immediately transform it into the required "
        "social media posts. Output the final posts directly."
    ),
    allow_delegation=False,
    verbose=True,
    llm=local_llm,
    memory=False
)