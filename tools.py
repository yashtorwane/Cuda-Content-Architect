import re
from crewai.tools import BaseTool
from youtube_transcript_api import YouTubeTranscriptApi

class YouTubeScraperTool(BaseTool):
    name: str = "YouTube Transcript Scraper"
    description: str = "MUST USE this tool to extract text from a YouTube video. Pass the URL."

    def _run(self, **kwargs) -> str:
        try:
            # 1. Extract the Video ID
            raw_input = str(kwargs)
            video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", raw_input)
            
            if not video_id_match:
                return "CRITICAL ERROR: Could not extract video ID."
            
            video_id = video_id_match.group(1)
            
            # 2. THE HACK: Ask YouTube for the English translation first!
            # English tokens will process 10x faster on your local GPU.
            ytt_api = YouTubeTranscriptApi()
            fetched_transcript = ytt_api.fetch(video_id, languages=['en', 'hi'])
            transcript_data = fetched_transcript.to_raw_data()
            
            # 3. Join the text
            full_text = " ".join([snippet['text'] for snippet in transcript_data])
            
            # 4. Truncate to ensure we never hit the 10-minute timeout again
            return full_text[:3000] + " ... [TRUNCATED FOR MEMORY LIMITS]"
        
        except Exception as e:
            return f"CRITICAL ERROR: {str(e)}. DO NOT make up a fake transcript."