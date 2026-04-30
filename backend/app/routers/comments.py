from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/tickets", tags=["comments"])


@router.post("/{ticket_id}/comments", response_model=schemas.Comment)
def create_comment(ticket_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    db_ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")

    db_comment = models.Comment(**comment.dict(), ticket_id=ticket_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
