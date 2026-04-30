from sqlalchemy import Column, Integer, String, Text, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(Enum("bug", "feature", "question", name="category_types"), nullable=False)
    priority = Column(Enum("low", "medium", "high", "critical", name="priority_levels"), nullable=False)
    status = Column(Enum("open", "pending", "resolved", "closed", name="status_types"), default="open", nullable=False)
    assignee = Column(String(100))
    reporter = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    comments = relationship("Comment", back_populates="ticket", cascade="all, delete-orphan")
