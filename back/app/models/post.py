'''Define table for posts made by user'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
from .user import User

class Post(Base):
    '''Define the post table'''
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    subject = Column(String(150), nullable=True)
    body = Column(String(1000), nullable=False)
    author_id = Column(
        Integer,
        ForeignKey('{}.id'.format(User.__tablename__)),
        index=True,
        nullable=False,
    )
    author = relationship(
        User,
        foreign_keys=[author_id],
        backref='posts',
    )
