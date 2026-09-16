import os
import requests
from dotenv import load_dotenv

# 1. Unlock Vault
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# 2. The specific URL to ask for available models
url = "https://api.groq.com/openai/v1/models"
headers = {
    "Authorization": f"Bearer {api_key}"
}

# 3. Send a GET request (we are just asking for data, not sending a payload)
print("Asking Groq for active models...\n")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("--- ACTIVE MODELS YOU CAN USE ---")
    # Loop through the data and print the exact ID of every active model
    for model in data["data"]:
        print(model["id"])
    print("---------------------------------")
else:
    print(f"Failed to get models. Status: {response.status_code}")