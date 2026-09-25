import os
from pathlib import Path
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import engine, Base, get_db
from routers import tickets, comments

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Helpdesk API",
    description="Backend for a mini helpdesk web application",
    version="1.0.0",
)

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://localhost:3000,*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes mounted under /api
app.include_router(tickets.router, prefix="/api")
app.include_router(comments.router, prefix="/api")

# Also keep /tickets and /comments without prefix for backwards compatibility
app.include_router(tickets.router)
app.include_router(comments.router)


@app.get("/api/db-check")
@app.get("/db-check")
def db_check(db=Depends(get_db)):
    try:
        # 1. Základní test spojení
        from sqlalchemy import text
        db.execute(text("SELECT 1"))
        
        # 2. Test čtení dat (pokus o načtení prvního ticketu)
        import models
        first_ticket = db.query(models.Ticket).first()
        
        ticket_info = "Žádné tickety v databázi nenalezeny."
        if first_ticket:
            ticket_info = f"Nalezen ticket #{first_ticket.id}: {first_ticket.title} (Reporter: {first_ticket.reporter})"
            
        return {
            "status": "success", 
            "message": "Databáze je připojena a funkční!",
            "database_test": ticket_info
        }
    except Exception as e:
        return {"status": "error", "message": f"Chyba databáze: {str(e)}"}


# Static files (Vue SPA production build)
DIST_DIR = Path(__file__).resolve().parent / "dist"

if DIST_DIR.exists():
    assets_dir = DIST_DIR / "assets"
    if assets_dir.exists():
        app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="assets")

    @app.get("/{full_path:path}")
    def serve_spa(full_path: str):
        # Serve existing static files in dist (e.g. favicon.ico, vite.svg)
        potential_file = DIST_DIR / full_path
        if full_path and potential_file.is_file():
            return FileResponse(str(potential_file))
        # Fallback to index.html for Vue Router
        return FileResponse(str(DIST_DIR / "index.html"))
else:
    @app.get("/")
    def root():
        return {"message": "Welcome to Helpdesk API. Go to /docs for API documentation."}

