from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import tickets, comments

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
