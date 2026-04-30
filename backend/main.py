import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base, get_db
from routers import tickets, comments

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Helpdesk API",
    description="Backend for a mini helpdesk web application",
    version="1.0.0",
)

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tickets.router)
app.include_router(comments.router)


@app.get("/")
def root():
    return {"message": "Welcome to Helpdesk API. Go to /docs for API documentation."}


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
