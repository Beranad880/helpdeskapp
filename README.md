# 🛠️ Mini Helpdesk Web Application

A modern, full-stack helpdesk solution designed for simplicity and efficiency. Built with **FastAPI** on the backend and **Vue.js 3** on the frontend.

---

## 🚀 Features

- **📊 Smart Dashboard**: Instantly view ticket statistics (Open, Pending, Resolved, Closed).
- **🎫 Ticket Management**: 
  - List view with advanced filtering by **Status** and **Priority**.
  - Detailed ticket views with full history.
  - Category-based sorting (Bug, Feature, Question).
- **💬 Interactive Comments**: Real-time communication on every ticket.
- **⚡ Fast UI**: Built with Vue 3 (Composition API) and Vite for a lightning-fast experience.
- **🐳 Docker Ready**: Fully containerized with Docker Compose for one-click setup.
- **📜 API Documentation**: Automatically generated OpenAPI (Swagger) docs.

---

## 🏗️ Project Structure

```text
helpdeskapp/
├── backend/            # FastAPI, SQLAlchemy, MySQL
│   ├── routes/         # API Endpoints
│   ├── main.py         # Entry point
│   └── models.py       # Database Schema
├── frontend/           # Vue.js 3, Vite, Axios
│   ├── src/
│   │   ├── views/      # Page Components
│   │   └── api/        # Axios Client
│   └── index.html
└── docker-compose.yml  # Orchestration
```

---

## 💻 Local Installation

### 1. Backend Setup (FastAPI)
1. **Navigate to backend:** `cd backend`
2. **Setup environment:** Create `.env` file (see `.env.example`).
   ```env
   DATABASE_URL=mysql+pymysql://user:password@localhost:3306/helpdesk
   ```
3. **Install & Run:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```
   📍 API Docs: `http://localhost:8000/docs`

### 2. Frontend Setup (Vue.js 3)
1. **Navigate to frontend:** `cd frontend`
2. **Setup environment:** Create `.env` file.
   ```env
   VITE_API_URL=http://localhost:8000
   ```
3. **Install & Run:**
   ```bash
   npm install
   npm run dev
   ```
   📍 App URL: `http://localhost:5173`

---

## 🐳 Running with Docker

The easiest way to get started:
```bash
docker-compose up --build
```
- **Frontend**: `http://localhost`
- **Backend API**: `http://localhost:8000`

---

## ☁️ Deployment (Railway)

### Backend
1. Connect your GitHub repo to Railway.
2. Add a **MySQL** plugin.
3. Set the `DATABASE_URL` variable to point to the MySQL plugin.
4. Set the Root Directory to `backend`.

### Frontend
1. Add a new service from the same repo.
2. Set the `VITE_API_URL` to your backend's public URL.
3. Set the Root Directory to `frontend`.

---

## 📝 Troubleshooting

- **Import Errors?** Ensure you are running `uvicorn` from the `backend/` directory or use `python -m uvicorn backend.main:app`.
- **Database Connection?** Verify your MySQL server is running and the credentials in `.env` are correct.
- **CORS Issues?** The backend is configured to allow `*` by default, but you can restrict it in `main.py`.

---
*Developed with help using Gemini CLI, Claude Code*
