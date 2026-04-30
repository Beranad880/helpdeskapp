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
├── backend/            # FastAPI Project Root
│   ├── models/         # Database models
│   ├── routers/        # API routes
│   ├── schemas/        # Pydantic schemas
│   ├── main.py         # Entry point
│   ├── database.py     # DB config
│   └── .env            # Backend secrets
├── frontend/           # Vue.js 3 Project Root
└── docker-compose.yml
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
   
   # Run uvicorn from the backend/ directory
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

## ☁️ Deployment to Railway (Step-by-Step)

Since you are deploying the backend and frontend as **two separate services**, follow these steps:

### 1. Backend Service
1. Create a new service on Railway from your repository.
2. Set the **Root Directory** to `backend`.
3. Go to the **Variables** tab and add:
   - `DATABASE_URL`: Your MySQL connection string (e.g., `mysql+pymysql://user:pass@host:port/db`).
4. Railway will automatically detect the `Dockerfile` and deploy it.
5. **Note your Public URL** (e.g., `https://backend-production.up.railway.app`).

### 2. Frontend Service
1. Create another service from the same repository.
2. Set the **Root Directory** to `frontend`.
3. Go to the **Variables** tab and add:
   - `VITE_API_URL`: The **Public URL of your Backend** (e.g., `https://backend-production.up.railway.app`).
4. **Crucial:** You must set this variable **before** the build starts, as Vite injects it during the build process.
5. Railway will build the production static files and serve them via Nginx.

---

## 📝 Troubleshooting

- **Frontend can't reach Backend?** Double check that `VITE_API_URL` in Railway variables does **not** have a trailing slash (e.g., use `...railway.app` instead of `...railway.app/`).
- **Database errors?** Make sure you are using the `mysql+pymysql://` prefix in your `DATABASE_URL` so SQLAlchemy knows which driver to use.
- **CORS?** The backend is currently set to `allow_origins=["*"]`, which works for any frontend URL.

---
