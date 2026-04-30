from pydantic import BaseModel
from datetime import datetime


class CommentBase(BaseModel):
    author: str
    text: str


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    ticket_id: int
    created_at: datetime

    class Config:
        orm_mode = True
