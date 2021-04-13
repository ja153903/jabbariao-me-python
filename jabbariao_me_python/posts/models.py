import datetime
from sqlalchemy import Boolean, Integer, DateTime, String, Column, Table, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base

post_tag_association_table = Table('post_tag_association', Base.metadata,
    Column("post_id", Integer, ForeignKey("post.id")),
    Column("tag_id", Integer, ForeignKey("tag.id")),
)


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    post = Column(String)
    published = Column(Boolean, default=False)

    created_at = Column("createdAt", DateTime, default=datetime.datetime.utcnow)
    updated_at = Column("updatedAt", DateTime, onupdate=datetime.datetime.utcnow)

    tags = relationship("Tag", secondary=post_tag_association_table)


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
