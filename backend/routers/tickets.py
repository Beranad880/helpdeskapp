from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas
from database import get_db

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.get("/stats")
def read_ticket_stats(db: Session = Depends(get_db)):
    from sqlalchemy import func
    # Explicitly get the value of the Enum for the key
    status_stats = db.query(models.Ticket.status, func.count(models.Ticket.id)).group_by(models.Ticket.status).all()
    priority_stats = db.query(models.Ticket.priority, func.count(models.Ticket.id)).group_by(models.Ticket.priority).all()

    # Ensure keys are simple strings
    return {
        "status": {str(s if isinstance(s, str) else s.value if s else ""): c for s, c in status_stats},
        "priority": {str(p if isinstance(p, str) else p.value if p else ""): c for p, c in priority_stats}
    }



@router.get("", response_model=List[schemas.TicketSummary])
@router.get("/", response_model=List[schemas.TicketSummary])
def read_tickets(
    status: Optional[schemas.TicketStatus] = Query(None),
    priority: Optional[schemas.TicketPriority] = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(models.Ticket)
    if status:
        query = query.filter(models.Ticket.status == status)
    if priority:
        query = query.filter(models.Ticket.priority == priority)
    return query.order_by(models.Ticket.id.desc()).all()


@router.get("/{ticket_id}", response_model=schemas.Ticket)
@router.get("/{ticket_id}/", response_model=schemas.Ticket)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket


@router.post("", response_model=schemas.TicketSummary)
@router.post("/", response_model=schemas.TicketSummary)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):

    try:
        ticket_data = ticket.model_dump()
        # Ensure enums are converted to their string values for SQLAlchemy
        if hasattr(ticket_data.get("category"), "value"):
            ticket_data["category"] = ticket_data["category"].value
        if hasattr(ticket_data.get("priority"), "value"):
            ticket_data["priority"] = ticket_data["priority"].value

        db_ticket = models.Ticket(**ticket_data)
        db.add(db_ticket)
        db.commit()
        db.refresh(db_ticket)
        return db_ticket
    except HTTPException:
        db.rollback()
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error while saving ticket: {str(e)}"
        )



@router.patch("/{ticket_id}", response_model=schemas.Ticket)
@router.patch("/{ticket_id}/", response_model=schemas.Ticket)
def update_ticket(ticket_id: int, ticket: schemas.TicketUpdate, db: Session = Depends(get_db)):

    db_ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")

    for key, value in ticket.model_dump(exclude_unset=True).items():
        setattr(db_ticket, key, value)

    db.commit()
    db.refresh(db_ticket)
    return db_ticket
