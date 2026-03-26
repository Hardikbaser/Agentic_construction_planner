🏗️ Construction Planning Assistant Agent
📌 Problem Statement

Construction projects involve complex planning, scheduling, and resource management. Manual planning is time-consuming, error-prone, and inefficient.

This project builds an AI-powered Construction Planning Assistant that automatically generates:

Actionable construction plans
Execution schedules
Resource-aware task breakdowns
🎯 Project Objectives
Automate construction planning using AI agents
Generate structured task breakdowns from high-level goals
Provide optimized scheduling based on available resources
Integrate external knowledge (RAG + web scraping)
Deliver a simple, professional frontend interface
📦 Scope of the Project

This system focuses on:

Planning workflows (not actual execution)
AI-driven decision support
Small-to-medium construction scenarios
💡 Proposed Solution
🔑 Key Features
AI-powered Planning Agent
AI-powered Scheduling Agent
RAG (Retrieval-Augmented Generation) for construction rules
Web Scraping for real-time data
Resource Awareness (labor availability)
Interactive Frontend UI
FastAPI Backend APIs
⚙️ System Architecture / Workflow
User Input (Frontend)
        ↓
FastAPI Backend
        ↓
Planner Agent → (RAG + Web Data)
        ↓
Generated Plan
        ↓
Scheduler Agent → (Resource Check)
        ↓
Execution Schedule
        ↓
Frontend Display
🛠️ Tools & Technologies Used
🔹 Backend
Python
FastAPI
CrewAI (Multi-agent system)
LangChain
Groq API (LLM - LLaMA3)
🔹 AI & Data
RAG (ChromaDB)
HuggingFace Embeddings
Web Scraping
🔹 Frontend
HTML
CSS
JavaScript
🔹 Environment
Virtual Environment (venv)
dotenv (.env for API keys)
📊 Features Explained
1️⃣ Planner Agent
Converts user goals into detailed construction steps
Uses:
RAG for rules
Web scraping for additional context
2️⃣ Scheduler Agent
Converts plan into execution schedule
Considers:
Resource availability (e.g., labor)
3️⃣ RAG System
Retrieves relevant construction guidelines
Improves accuracy of plans
4️⃣ Web Scraper
Fetches latest construction-related info
Enhances real-world relevance
5️⃣ Frontend UI
Clean input box for user goals
Buttons:
Generate Plan
Generate Schedule
Displays structured output
🚀 How to Run the Project
1️⃣ Clone the Repository
git clone <your-repo-link>
cd project-folder
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
pip install litellm
4️⃣ Set Environment Variables

Create a .env file:

GROQ_API_KEY=your_api_key_here
5️⃣ Run the Server
uvicorn main:app --reload
6️⃣ Open in Browser
http://127.0.0.1:8000
🧪 Sample Inputs

Try these:

"Build a residential house"
"Permit requirements for commercial building"
"Road construction planning"
"Bridge construction workflow"
📤 Output Example
📋 Plan
Site inspection
Design approval
Material procurement
Foundation work
Structural construction
📅 Schedule
Day 1–3: Inspection
Day 4–10: Permits
Day 11–20: Foundation
Day 21–40: Construction
