import datetime
from typing import List, Optional

from pydantic import BaseModel


class TagBase(BaseModel):
    name: str


class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str
    post: str


class Post(PostBase):
    id: int
    created_at: datetime.datetime
    tags: Optional[List[Tag]]

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass