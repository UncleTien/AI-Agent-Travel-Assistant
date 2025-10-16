# 🧭 Agent Travel Assistant

### ✨ Overview
**Agent Travel Assistant** is an intelligent AI application that helps users automatically **generate personalized travel itineraries** from natural language input.  
The system includes:
- 🧠 **Backend (FastAPI)** — Handles user queries and interacts with LLMs (OpenAI or Ollama).
- 🌐 **Frontend (React + Vite)** — Simple and interactive user interface.
- 🐳 **Docker (optional)** — For easy and consistent deployment.

---

## 📁 Project Structure
```
AgentTravelAssistant/
│
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── routes/          # API routes (chat, LLM handler, etc.)
│   │   ├── core/            # Configurations & utilities
│   │   ├── agents/          # LLM agent logic
│   │   └── main.py          # FastAPI entrypoint
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/                # React + Vite frontend
│   ├── src/
│   ├── vite.config.js
│   ├── package.json
│   └── .env.example
│
├── docker-compose.yml       # (Optional) Docker setup
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 Requirements
- Python **3.10+**
- Node.js **18+**
- (Optional) Docker & Docker Compose

---

## 🧠 1. Backend Setup (FastAPI)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

Create a `.env` file based on the example:
```bash
cp .env.example .env
```

Then edit `.env`:
```bash
# BACKEND
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o-mini
LLM_BACKEND=openai           # or ollama
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

# FRONTEND
VITE_API_BASE=http://localhost:8000
```

Run the server:
```bash
uvicorn app.main:app --reload
```

Backend runs at 👉 **http://localhost:8000**

---

## 💻 2. Frontend Setup (React + Vite)

```bash
cd frontend
npm install
```

Create `.env`:
```bash
cp .env.example .env
```

Edit it:
```bash
VITE_API_BASE=http://localhost:8000
```

Run the development server:
```bash
npm run dev
```

Frontend runs at 👉 **http://localhost:5173**

---

## 🐳 3. (Optional) Docker Setup

Run the entire stack via Docker Compose:
```bash
docker compose up --build
```

---

## 🧩 4. LLM Integration
Option 1: **OpenAI API**
- Set your `OPENAI_API_KEY`
- Set `LLM_BACKEND=openai`

Option 2: **Ollama (local model)**
- Install [Ollama](https://ollama.ai)
- Pull model:
  ```bash
  ollama pull llama3.2
  ```
- Set:
  ```bash
  LLM_BACKEND=ollama
  OLLAMA_URL=http://localhost:11434
  ```

---

## 🚀 Run the App
Open your browser and go to:
```
http://localhost:5173
```
Example query:
> “Plan a 3-day trip to Da Nang”

The AI will automatically generate a travel itinerary for you. 🌴