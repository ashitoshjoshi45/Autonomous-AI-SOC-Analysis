import os
from datetime import datetime
from dotenv import load_dotenv
import ollama  # <--- Changed this

# 1. Setup Environment
load_dotenv()
# Note: Local Ollama usually doesn't need a key, but we'll keep your check logic
api_key = os.getenv('Ollama_API_KEY') 

# 2. Define Colors
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

# 3. Define the Analyst Function
def analyze_logs(file_path):
    with open(file_path, 'r') as file:
        log_data = file.read()

    prompt = f"""
    You are a Senior SOC Analyst. 
    Analyze the following logs and provide a RISK SCORE (1-10) and a THREAT LEVEL (Low, Medium, High, Critical).
    
    LOG DATA:
    {log_data}
    """
    
    # 4. Use Ollama instead of Gemini
    # Make sure you have the model downloaded (e.g., 'ollama run llama3' in terminal)
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    
    analysis_text = response['message']['content']
    
    # Logic for color and timestamp
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if "Critical" in analysis_text or "High" in analysis_text:
        color = RED
    elif "Medium" in analysis_text:
        color = YELLOW
    else:
        color = GREEN

    # 5. Print the Final Report
    print("\n" + "="*40)
    print(f"REPORT GENERATED: {now}")
    print(f"{color}AI SOC ANALYST ENGINE (OLLAMA LOCAL){RESET}")
    print("="*40)
    print(f"{color}{analysis_text}{RESET}")

analyze_logs('sample_logs.txt')