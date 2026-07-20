import os
import json
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
# Using the key name from your .env file
API_KEY = os.getenv("Ollama_API_KEY") 

# Terminal Colors for Dashboard Output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

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
        
        # System instructions set the 'persona' and rules for the AI
        system_prompt = """
        You are an AI Security Analyst (SOC Bot). 
        Analyze the incoming network request log for security threats.
        Output ONLY a JSON object with this exact structure:
        {
            "verdict": "SAFE", "SUSPICIOUS", or "MALICIOUS",
            "attack_type": "SQL Injection", "SSH Brute Force", "XSS", or "None",
            "confidence": <number 0-100>,
            "reasoning": "<short explanation>"
        }
        """
        
        user_query = f"Analyze log:\nIP: {ip_address}\nPort: {port}\nPayload: {payload}"

        # Using Gemini 2.5 Flash for the best balance of speed and reasoning
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=user_query,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                response_mime_type="application/json"
            )
        )

        # Parse the JSON response text into a Python dictionary
        return json.loads(response.text)

    except Exception as e:
        print(f"[-] Gemini API Error: {e}")
        # Fallback logic if API fails or rate limit is hit
        if any(k in payload.upper() for k in ["SELECT", "DROP", "DEBUG", "<SCRIPT>"]):
            return {
                "verdict": "MALICIOUS",
                "attack_type": "Heuristic Match",
                "confidence": 50,
                "reasoning": "API Failed. Local rule caught suspicious keyword."
            }
        return {
            "verdict": "BENIGN", 
            "attack_type": "None", 
            "confidence": 100, 
            "reasoning": "Default safe response on API error."
        }

def process_logs(log_file):
    """
    Reads a log file and processes each line through the AI Analyst.
    """
    print(f"[*] Starting Autonomous SOC Analyst on '{log_file}'...\n")
    print("-" * 60)
    try:
        with open(log_file, "r") as file:
            for line in file:
                # Clean the line
                line = line.strip()
                if not line:
                    continue

                # Expected format: "192.168.1.1 80 SELECT * FROM users"
                # This splits by the first two spaces to get IP, Port, and Payload
                parts = line.split(" ", 2)
                
                if len(parts) < 3:
                    print(f"[!] Skipping malformed line: {line}")
                    continue

                ip, port, payload = parts

                # analyze_threat already returns a dictionary, so we just save it to 'result'
                result = analyze_threat(ip, payload, port)

                # Safely get the verdict
                verdict = result.get("verdict", "UNKNOWN").upper()
                
                # Pick a color based on the threat level
                if verdict == "MALICIOUS":
                    color = RED
                elif verdict == "SUSPICIOUS":
                    color = YELLOW
                else:
                    color = GREEN
                
                # Print the professional dashboard output
                print(f"{color}[{verdict}]{RESET} {ip}:{port} | Threat: {result.get('attack_type')}")
                print(f"Reasoning: {result.get('reasoning')}")
                print("-" * 60)
                
                # Sleep for 2 seconds to avoid hitting the free API rate limit
                time.sleep(2) 

    except FileNotFoundError:
        print(f"[-] Error: The file '{log_file}' was not found.")

if __name__ == "__main__":
    # Ensure sample_logs.txt exists in the same directory
    process_logs("sample_logs.txt")