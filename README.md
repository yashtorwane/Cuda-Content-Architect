🏎️ Cuda-Content-Architect: High-Performance Local AI Agent Squad
![Execution Proof](./assets/gpu_screenshot.png)
Cuda-Content-Architect is a privacy-first, zero-cost, and hardware-accelerated AI multi-agent system. It transforms long-form YouTube intelligence into high-signal social media assets (LinkedIn/X) using 100% local inference. No cloud APIs, no subscription fees, and no data latency.

------------------------------------------------------------------------------------------------------------------------------------


🏗️ System Architecture & Workflow

The system employs an autonomous multi-agent sequential pipeline orchestrated via CrewAI:

Lead Video Researcher:
* Function: Deep-data extraction from raw YouTube transcripts.
  
* Engineering: Features a custom Data Truncation Engine to optimize token density for local VRAM limits.

* Capability: Processes multi-language transcripts (English/Hindi) with automatic synthesis logic.


Social Media Architect:
* Function: Creative synthesis and brand-voice alignment.
 
* Output: Generates 5 high-impact LinkedIn posts and 2 viral Twitter threads using a "Helpful Peer" tone.

  
------------------------------------------------------------------------------------------------------------------------------------



🔥 Hardware-Acceleration Flex
This project is engineered to pin local silicon. During the synthesis phase on an NVIDIA RTX 4050 (6GB VRAM), the system achieves:

89% GPU Utilization: Directly offloading cognitive tasks to CUDA cores for near-instant inference.

VRAM Management: Successfully optimized to run entirely within 3.9GB of Dedicated VRAM, ensuring 0% reliance on slower system RAM.
Proof of Work: See visual evidence in the /assets folder.


------------------------------------------------------------------------------------------------------------------------------------


🛠️ The Tech Stack

Orchestration: CrewAI (Agentic Workflow Framework)

Local LLM Server: Ollama (Llama 3.2 3B)

Frontend: Streamlit (Web Dashboard UI)

Compute: NVIDIA CUDA (Hardware-accelerated inference)

Tooling: Custom Python Scraper (Regex + Object-Oriented YouTube API)

------------------------------------------------------------------------------------------------------------------------------------


🚀 Setup & Installation
1. Model Preparation
Install Ollama and pull the optimized weights:

Bash

ollama pull llama3.2

3. Environment Setup
Bash

git clone https://github.com/yashtorwane/Cuda-Content-Architect.git

cd Cuda-Content-Architect

# Install dependencies

pip install -r requirements.txt


3. Launching the Dashboard 🏎️

Launch the web interface to begin generating content:

Bash

streamlit run app.py



------------------------------------------------------------------------------------------------------------------------------------


🛡️ Engineering Guardrails To ensure production-grade reliability on consumer-grade hardware:

Anti-Hallucination Logic: Strict "Force Feed" instructions to prevent LLM fabrications if transcripts are unavailable.

Token Optimization: Hybrid truncation logic to maintain the context window within the 128k Llama 3.2 limit.

Regex-based ID Extraction: Bulletproof identification of 11-character YouTube video IDs.

------------------------------------------------------------------------------------------------------------------------------------


Developed by Yash Bhagwan Torwane. 

------------------------------------------------------------------------------------------------------------------------------------



💡 Engineering Note
This project was developed as a case study in Edge AI Engineering, focusing on how to deploy agentic workflows on consumer-grade hardware without relying on centralized cloud providers.
