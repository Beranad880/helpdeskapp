from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List, Optional
from enum import Enum
from schemas.comment import Comment


class TicketCategory(str, Enum):
    bug = "bug"
    feature = "feature"
    question = "question"


class TicketPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class TicketStatus(str, Enum):
    open = "open"
    pending = "pending"
    resolved = "resolved"
    closed = "closed"


class TicketBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    description: str
    category: TicketCategory
    priority: TicketPriority
    reporter: str
    assignee: Optional[str] = None


class TicketCreate(TicketBase):
    pass


class TicketUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    status: Optional[TicketStatus] = None
    priority: Optional[TicketPriority] = None
    assignee: Optional[str] = None


class TicketSummary(TicketBase):
    id: int
    status: TicketStatus
    created_at: datetime


class Ticket(TicketSummary):
    comments: List[Comment] = []


class TicketPage(BaseModel):
    items: List[TicketSummary]
    total: int
    page: int
    limit: int
