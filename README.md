# FAANG Python Interview Simulator 🚀

A CLI-based conversational AI agent that stress-tests developers on core Python mechanics by simulating a strict FAANG Engineering Manager.

## 🧠 The Architecture

Large Language Models (LLMs) are inherently amnesic. This project overcomes that limitation by implementing a custom state-management architecture from scratch, allowing the AI to remember the user, maintain context, and execute specialized evaluation tasks over a continuous session.

### Core Features
* **Stateful Memory Stack:** Dynamically appends user inputs and AI responses into a JSON dictionary list, passing the entire chronological transcript to the server on every loop.
* **Persona-Driven Prompting:** Injects a strict System Directive (`role: system`) at the top of the memory stack to enforce the interviewer persona and conversation rules.
* **Cost-Optimized Payloads:** Implements strict token budgeting (`max_tokens: 300`) to protect API unit economics, prevent "blank check" requests, and avoid rate-limit crashes (HTTP 429).
* **Dynamic Engine Routing:** Designed to gracefully handle model deprecations by routing to active, high-efficiency models via the Groq API (currently running `qwen/qwen3.8-27b`).

## 🛠️ Tech Stack
* **Language:** Python 3
* **Infrastructure:** Groq API
* **Libraries:** `requests`, `python-dotenv`

## 🚀 How to Run It Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/faang-interview-simulator.git](https://github.com/YO/faang-interview-simulator.git)
   cd faang-interview-simulator