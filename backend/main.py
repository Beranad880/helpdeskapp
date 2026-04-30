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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
        # Execute a simple query to check connection
        from sqlalchemy import text
        db.execute(text("SELECT 1"))
        return {"status": "success", "message": "Database connection is working!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
