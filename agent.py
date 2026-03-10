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

# Researcher Agent (Local)
researcher = Agent(
    role='Lead Video Researcher',
    goal='Extract high-impact viral hooks and key business insights from the {youtube_url} transcript.',
    backstory=(
        'You are an expert content strategist. The video transcript is in Hindi. '
        'You MUST read the Hindi text, explicitly translate the core business concepts '
        '(like market penetration and diversification) into English, and summarize them '
        'accurately in bullet points. DO NOT make up fictional stories about a dentist.'
    ),
    allow_delegation=False,
    verbose=True,
    tools=[scraper_tool], 
    llm=local_llm, 
    memory=False
)

# Writer Agent (Local)
writer = Agent(
    role='Social Media Architect',
    goal='Transform the extracted video insights into 2 professional LinkedIn posts and 1 short Twitter thread.',
    backstory=(
        'You are a master copywriter. Write professional, highly engaging content based '
        'STRICTLY on the researcher\'s notes. Avoid AI clichés. You must complete the task '
        'and output the final text.'
    ),
    allow_delegation=False,
    verbose=True,
    llm=local_llm, 
    memory=False
)