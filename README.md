# 🤖 Multi-Agent AI Task Manager

An AI-powered multi-agent system that helps users manage tasks, schedules, and notes using natural language by coordinating multiple agents and tools.

---

## 🧠 Overview

This project demonstrates a **multi-agent AI architecture** where a primary agent coordinates multiple specialized agents to complete user requests involving tasks, scheduling, and information retrieval.

Users can interact with the system using plain English, and the system intelligently breaks down requests into actions handled by different agents.

---

## 🎯 Problem Statement

Build a multi-agent AI system that helps users manage tasks, schedules, and information by interacting with multiple tools and data sources.

---

## 🚀 Key Features

- 🧠 Multi-agent coordination (Main Agent + Sub-agents)
- 📅 Calendar management
- ✅ Task tracking system
- 📝 Notes storage & retrieval
- 🔄 Multi-step workflow execution
- 🔧 Tool integration (MCP-style architecture)
- ☁️ Cloud-ready deployment (Google Cloud Run)

---

## 🏗️ Architecture

```

User Input
↓
Main Agent (Controller)
↓
-

↓              ↓              ↓
Task Agent   Calendar Agent   Notes Agent
↓              ↓              ↓
Task Tool     Calendar Tool   Notes Tool
----------------------------------------

```
↓
```

Database (AlloyDB / PostgreSQL)
↓
Response to User

```

---

## 🔄 Example Workflow

User Input:
```

Schedule a meeting tomorrow and add a task to prepare slides

```

System Execution:
- Main Agent interprets request
- Calendar Agent schedules meeting
- Task Agent creates task
- Data stored in database
- Combined response returned

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Agents:** Custom multi-agent system (LangGraph / modular agents)
- **LLM:** Gemini (Vertex AI)
- **Database:** PostgreSQL / AlloyDB
- **Deployment:** Google Cloud Run
- **Architecture:** MCP-style tool integration

---

## 📂 Project Structure

```

multi-agent-ai/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── agents/
│   ├── main_agent.py
│   ├── task_agent.py
│   ├── calendar_agent.py
│   └── notes_agent.py
│
├── tools/
│   ├── task_tool.py
│   ├── calendar_tool.py
│   └── notes_tool.py
│
├── db/
│   ├── db.py
│   └── schema.sql
│
├── services/
│   └── llm.py

````

---

## ⚙️ How It Works

1. User sends natural language query
2. Main agent analyzes intent
3. Routes request to appropriate sub-agents
4. Sub-agents use tools to perform actions
5. Data stored/retrieved from database
6. Final response returned to user

---

## 🔐 Authentication

- Uses Google Cloud IAM (for Vertex AI)
- Secure backend communication

---

## 🚀 Running Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
````

---

### 2. Run the app

```bash
uvicorn app:app --reload
```

---

### 3. Open API

```
http://localhost:8000
```

---

## ☁️ Deploy to Cloud Run

```bash
gcloud builds submit --tag gcr.io/<PROJECT_ID>/multi-agent-ai

gcloud run deploy multi-agent-ai \
  --image gcr.io/<PROJECT_ID>/multi-agent-ai \
  --region=us-central1 \
  --allow-unauthenticated
```

---

## 🧠 Key Learnings

* Designing multi-agent AI systems
* Coordinating agents and tools
* Building scalable AI APIs
* Integrating LLMs with real-world workflows
* Cloud-native deployment

---

## 🚀 Future Improvements

* 💬 Chat-based UI
* 📊 Dashboard & analytics
* 🔎 Vector search for notes
* 📅 Real Google Calendar integration
* 🔔 Notifications system

---

## 👨‍💻 Author

**Sajjan Mali**
B.Tech CSE, IIIT Manipur

---

## 🏆 Hackathon Project

Built for a **Multi-Agent AI Hackathon Challenge**

---

## ⭐ Final Note

This project showcases how multi-agent systems can collaborate with tools and databases to solve real-world productivity problems using AI.

---
