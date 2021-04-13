from typing import Optional, List
from sqlalchemy.orm import Session

from . import models, schemas

def get_post(db: Session, post_id: int) -> Optional[schemas.Post]:
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_all_posts(db: Session) -> List[schemas.Post]:
    return db.query(models.Post).order_by(models.Post.created_at.desc()).all()

def get_latest_posts(db: Session, n: int = 5):
    return db.query(models.Post).order_by(models.Post.created_at.desc()).limit(n).all()