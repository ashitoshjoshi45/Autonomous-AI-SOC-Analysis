import os
import json
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
API_KEY = os.getenv("Ollama_API_KEY") # Matching your .env name

def analyze_threat(ip_address, payload, port):
    """
    Sends the log data to Google Gemini and returns a structured JSON analysis.
    """
    if not API_KEY:
        return {
            "verdict": "ERROR",
            "attack_type": "None",
            "confidence": 0,
            "reasoning": "API Key missing in .env"
        }

    try:
        # Initialize the Client
        client = genai.Client(api_key=API_KEY)
        
        system_prompt = """
        You are an AI Security Analyst (SOC Bot). 
        Analyze the incoming network request log for security threats.
        Output ONLY a JSON object with this exact structure:
        {
            "verdict": "SAFE" or "MALICIOUS",
            "attack_type": "SQL Injection", "SSH Brute Force", "XSS", or "None",
            "confidence": <number 0-100>,
            "reasoning": "<short explanation>"
        }
        """
        
        user_query = f"Analyze log:\nIP: {ip_address}\nPort: {port}\nPayload: {payload}"

        # Using the Gemini 2.0 Flash model for speed/cost efficiency
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=system_prompt + "\n\n" + user_query,
            config={
                "response_mime_type": "application/json" 
            }
        )

        # Parse the JSON response
        # The new genai library returns a response object; we extract the text and load as dict
        return json.loads(response.text)

    except Exception as e:
        print(f"[-] Gemini API Error: {e}")
        # Fallback to Mock Logic if API fails
        if any(k in payload.upper() for k in ["SELECT", "DROP", "DEBUG"]):
            return {
                "verdict": "MALICIOUS",
                "attack_type": "Mock Injection",
                "confidence": 50,
                "reasoning": f"API Failed. Mock caught keyword. Error: {e}"
            }
        return {
            "verdict": "BENIGN", 
            "attack_type": "None", 
            "confidence": 100, 
            "reasoning": "Default safe response on API error."
        }