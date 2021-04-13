from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db, engine
from . import schemas, crud, models

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/posts",
)

@router.get("/", response_model=List[schemas.Post])
def read_all_posts(db: Session = Depends(get_db)):
    posts = crud.get_all_posts(db)
    return posts

@router.get("/{post_id}", response_model=schemas.Post)
def read_post_by_id(post_id: int, db: Session = Depends(get_db)):
    post_by_id = crud.get_post(db, post_id)
    if post_by_id is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post_by_id

@router.get("/latest", response_model=List[schemas.Post])
def read_latest_posts(db: Session = Depends(get_db)):
    posts = crud.get_latest_posts(db)
    return posts