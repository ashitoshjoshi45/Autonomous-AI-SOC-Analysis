        
import os
import json
from google import genai
from dotenv import load_dotenv

# Load environment variables (API Key)
load_dotenv()

print("Debug: ai_analyst.py is loaded successfully")

try: 
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("CRITICAL ERROR: API_KEY_NOT FOUND IN .env file!")


# Initialize the new Client
# Make sure your .env file has GEMINI_API_KEY=your_key_here
    client = genai.Client(api_key=api_key)
except Exception as e:
    print(f"Error setting up Gemini Client: {e}")

def analyze_threat(ip_address, payload, port):
    """
    Sends the log data to Google Gemini and returns a JSON analysis.
    """
    try:
        # 1. Define the system instructions for the AI
        system_prompt = """
        You are an AI Security Analyst (SOC Bot). 
        Analyze the incoming network request log for security threats.
        
        Output ONLY a JSON object with the following structure:
        {
            "verdict": "SAFE" or "MALICIOUS",
            "attack_type": "SQL Injection", "SSH Brute Force", "XSS", or "None",
            "confidence": <number between 0-100>,
            "reasoning": "<short explanation of why>"
        }
        """
        
        # 2. Format the user's log data
        user_query = f"Analyze this log entry:\nIP Address: {ip_address}\nPort: {port}\nPayload: {payload}"

        # 3. Call the model
        # using 'gemini-1.5-flash' as it is fast and reliable for logs
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=system_prompt + "\n\n" + user_query,
            config={
                "response_mime_type": "application/json" 
            }
        )

        # 4. Return the parsed JSON
        # The new library automatically parses the JSON for us
        return response.parsed

    except Exception as e:
        # If something breaks (like no internet), return a safe error dict
        print(f"Error communicating with Gemini: {e}")
        return {
            "verdict": "ERROR",
            "attack_type": "System error",
            #"confidence": 0,
            "reasoning": str(e)
        }


