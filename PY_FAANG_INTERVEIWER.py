import os
import requests
from dotenv import load_dotenv

# 1. Unlock Vault & Setup
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 2. The Memory Stack (FAANG Interveiwer)
conversation_history = [
    {
        "role": "system", 
        "content" : "You are a strict but fair python Engineering Manager at a top FAANG company conducting a technical interveiw for a junior Developer role. Your goal is to evaluate the candidate's deep understanding of pyhton concepts.RULES: 1. Start the conversation by introducing yourself briefly and immediately asking the FIRST technical question. 2. Ask ONLY ONE question at a time. 3. Wait for the user to answer. 4. Analyze their answer. Critique it constructively, tell them if they passed or failed that specific question, and then ask the next technical question."

      
    }
]
print("FAANG Interveiwer online.Press Enter to start, or Type 'quit' to exit .\n")
# 3. Interaction_loop
while True:
    #3.1 Get user input
    user_prompt=input("You: ")

    if user_prompt.lower() == "quit":
        print("Ending Interveiw.Goodbye")
        break 

    # 3.2.Write User's message on notepad 
    conversation_history.append({"role" :"user","content":user_prompt }) 
    # 3.3 pack the payload with Entire notepad
    payload = {
        "model":"qwen/qwen3.8-27b",
        "messages" : conversation_history ,
        "max_tokens":300
    } 
    print("Manager is typing...") #
    #3.4 send the truck
    response=requests.post(url,headers=headers,json=payload)



# 4. Extract and Print


    if response.status_code == 200:
        data = response.json()
        ai_reply = data["choices"][0]["message"]["content"]
        print(f"\nManager: {ai_reply}\n")
        # write Ai reply to the notepad
        conversation_history.append({"role":"assistant","content":ai_reply})
    else:
        print(f"\n--- API ERROR ---")
        print(f"Status: {response.status_code}")
        print(f"Details: {response.text}")
        print(f"-----------------\n")
        # If the truck crashes, erase the last thing we wrote so we can try again
        conversation_history.pop()