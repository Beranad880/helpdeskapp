# 🛠️ Mini Helpdesk Web Application

Moderní full-stack helpdesk aplikace postavená na **FastAPI** (Python) na backendu a **Vue.js 3** (Vite) na frontendu s databází **MySQL**. Celá aplikace je připravena pro provoz v **jediném Docker kontejneru** (vhodné pro Railway, Render apod.) i pro pohodlný lokální vývoj.

---

## 🚀 Klíčové funkce

- **📊 Statistický dashboard**: Přehled stavu ticketů v reálném čase (Open, Pending, Resolved, Closed) a priority.
- **🎫 Správa ticketů**:
  - Filtrování podle stavu a priority.
  - Detail ticketu s kompletní historií a změnou stavu/priority.
  - Kategorizace (Bug, Feature, Question).
- **💬 Interaktivní komentáře**: Možnost přidávat komentáře k jednotlivým ticketům.
- **⚡ Moderní UI**: Vue.js 3 (Composition API), Vite, čistý CSS design.
- **🐳 Single Container Ready**: Multi-stage Dockerfile sestaví Vue frontend a servíruje ho přímo z FastAPI bez nutnosti samostatného Nginxu.
- **📜 Automatická API dokumentace**: Swagger UI na `/docs`.

---

## 🏗️ Struktura projektu

```text
helpdeskapp/
├── backend/                # FastAPI projekt
│   ├── models/             # SQLAlchemy databázové modely
│   ├── routers/            # API routy (/api/tickets, /api/comments)
│   ├── schemas/            # Pydantic validační schémata
│   ├── config.py           # Konfigurace prostředí
│   ├── database.py         # Připojení k DB (SQLAlchemy)
│   ├── main.py             # Vstupní bod FastAPI & SPA static files
│   └── requirements.txt    # Python závislosti
├── frontend/               # Vue.js 3 projekt
│   ├── src/
│   │   ├── api/            # Axios klient & API služby
│   │   ├── components/     # UI komponenty
│   │   ├── router/         # Vue Router (SPA navigace)
│   │   └── views/          # Stránky (Dashboard, List, Detail, New)
│   ├── package.json        # NPM závislosti a skripty
│   └── vite.config.js      # Vite konfigurace s dev proxy
├── .dockerignore           # Ignorované soubory při Docker buildu
├── Dockerfile              # Produkční multi-stage Dockerfile (Frontend + Backend)
└── README.md
```

---

## ☁️ Nasazení na Railway (Doporučeno: 1 kontejner)

Díky sjednocenému multi-stage Dockerfile stačí na Railway vytvořit **pouze 1 službu** a k ní přidat MySQL databázi. Není potřeba řešit CORS ani synchronizaci dvou URL adres.

### Krok 1: Vytvoření MySQL databáze
1. V projektu na [Railway](https://railway.app) klikněte na **+ New** -> **Database** -> **Add MySQL**.
2. Railway vytvoří spravovanou databázi.

### Krok 2: Vytvoření webové služby
1. V tom samém projektu klikněte na **+ New** -> **GitHub Repo** a vyberte tento repozitář.
2. V záložce **Settings**:
   - Ponechte **Root Directory** prázdné (Railway automaticky použije kořenový `Dockerfile`).
3. V záložce **Variables** přidejte pouze:
   - `DATABASE_URL`: `${{MySQL.DATABASE_URL}}`
4. V záložce **Settings** -> sekce **Networking**:
   - Klikněte na **Generate Domain** pro vytvoření veřejné HTTPS adresy.

Railway automaticky sestaví Vue aplikaci, nainstaluje Python závislosti a spustí aplikaci:
- **Webová aplikace**: `https://<vasedomena>.up.railway.app/`
- **Swagger API dokumentace**: `https://<vasedomena>.up.railway.app/docs`
- **Ověření připojení k DB**: `https://<vasedomena>.up.railway.app/api/db-check`

---

## 💻 Lokální spuštění (Vývoj)

Pro vývoj můžete backend i frontend spustit samostatně s funkcí hot-reload.

### 1. Backend (FastAPI)
1. Přejděte do složky backendu:
   ```bash
   cd backend
   ```
2. Vytvořte a aktivujte virtuální prostředí:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/macOS:
   source venv/bin/activate
   ```
3. Nainstalujte závislosti:
   ```bash
   pip install -r requirements.txt
   ```
4. Vytvořte soubor `.env` v adresáři `backend/`:
   ```env
   DATABASE_URL=mysql+pymysql://root:heslo@localhost:3306/helpdesk
   ```
5. Spusťte backend server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   📍 API Docs: `http://localhost:8000/docs`  
   📍 DB Check: `http://localhost:8000/api/db-check`

### 2. Frontend (Vue.js 3)
1. V novém terminálu přejděte do složky frontendu:
   ```bash
   cd frontend
   ```
2. Nainstalujte balíčky:
   ```bash
   npm install
   ```
3. Spusťte vývojový server:
   ```bash
   npm run dev
   ```
   📍 Aplikace běží na: `http://localhost:5173`  
   *(Vite je nakonfigurován tak, že veškerá volání na `/api` automaticky přeposílá na `http://localhost:8000`)*.

---

## 🐳 Lokální spuštění v Dockeru

Pokud chcete otestovat produkční sestavení lokálně před nasazením:

```bash
# 1. Sestavení Docker image
docker build -t helpdeskapp .

# 2. Spuštění kontejneru
docker run -p 8080:8080 -e DATABASE_URL="mysql+pymysql://user:password@host.docker.internal:3306/helpdesk" helpdeskapp
```
Aplikace bude dostupná na `http://localhost:8080`.
