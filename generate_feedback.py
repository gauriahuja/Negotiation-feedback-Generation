# import requests
# from dotenv import load_dotenv
# import os

# # === Load API Key from .env file ===
# load_dotenv()
# api_key = os.getenv("UF_AI_API_KEY")

# # === UF AI API Configuration ===
# API_URL = "https://api.ai.it.ufl.edu/v1/chat/completions"  # Confirm this with UF docs
# MODEL_NAME = "llama-3.3-70b-instruct"

# HEADERS = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }

# # === Example Function to Query UF AI ===
# def query_uf_ai(prompt: str, max_tokens: int = 300) -> str:
#     payload = {
#         "model": MODEL_NAME,
#         "messages": [
#             {"role": "user", "content": prompt}
#         ],
#         "temperature": 0.7,
#         "max_tokens": max_tokens,
#         "top_p": 0.9
#     }

#     response = requests.post(API_URL, headers=HEADERS, json=payload)
#     response.raise_for_status()
#     return response.json()["choices"][0]["message"]["content"].strip()

import os
import requests
from dotenv import load_dotenv

# Load .env and get API key
load_dotenv()
api_key = os.getenv("UF_AI_API_KEY")

if not api_key:
    print("API key not found. Check your .env file and variable name.")
    exit()

print("Loaded API Key:", api_key[:8], "...")

# Continue with API setup
API_URL = "https://api.ai.it.ufl.edu/v1/chat/completions"
MODEL_NAME = "llama-3.3-70b-instruct"
HEADERS = {
    "X-API-Key": api_key,
    "Content-Type": "application/json"
}



# === Function to Query UF API ===
def query_uf_ai(prompt: str, max_tokens: int = 300) -> str:
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": max_tokens,
        "top_p": 0.9
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()

# === Prompt Builders Based on Your Flowchart ===
def build_assessment_prompt(dialogue):
    return f"""
You are a negotiation coach. Based on the following dialogue, provide Assessment-Oriented Feedback.

Focus on:
- Confirmation: Did the negotiator validate or agree on key points?
- Corrective: What could have been done better?
- Explanatory: Can something be explained or clarified further?

Dialogue:
{dialogue}
"""

def build_process_prompt(dialogue):
    return f"""
You are a negotiation coach. Based on the following dialogue, provide Process-Based Feedback.

Focus on:
- Step-by-step actions taken
- Efficiency and use of time
- Strategic approach
- Adaptability to the partner’s messages
- Pacing of the negotiation

Dialogue:
{dialogue}
"""

def build_interaction_prompt(dialogue):
    return f"""
You are a negotiation coach. Based on the following dialogue, provide Interaction and Communication Feedback.

Focus on:
- Clarity of proposals
- Listening and responsiveness
- Follow-up on statements
- Building rapport and relationship tone

Dialogue:
{dialogue}
"""

# === Main Interactive Logic ===
if __name__ == "__main__":
    print("Welcome to the Negotiation Feedback Generator!")
    print("Enter the full dialogue (e.g., THEM: ... YOU: ...), or type 'exit' to quit.\n")

    while True:
        dialogue_input = input("🗣️  Enter your negotiation dialogue:\n")

        if dialogue_input.lower().strip() == "exit":
            print("Goodbye!")
            break

        print("\n Generating feedback...\n")

        # Generate all 3 feedback types
        assessment = query_uf_ai(build_assessment_prompt(dialogue_input))
        process = query_uf_ai(build_process_prompt(dialogue_input))
        interaction = query_uf_ai(build_interaction_prompt(dialogue_input))

        print("Assessment-Oriented Feedback:\n", assessment)
        print("\n Process-Based Feedback:\n", process)
        print("\n Interaction & Communication Feedback:\n", interaction)
        print("\n" + "-"*80 + "\n")
