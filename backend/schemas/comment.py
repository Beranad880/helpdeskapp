from pydantic import BaseModel, ConfigDict
from datetime import datetime


class CommentBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    author: str
    text: str


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    ticket_id: int
    created_at: datetime
