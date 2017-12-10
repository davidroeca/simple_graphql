'''Define the user model'''
from sqlalchemy import Column, Integer, String
from .base import Base

class User(Base):
    '''User Table'''

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    display_name = Column(String(100), nullable=True)
    username = Column(String(300), nullable=False, index=True)
    email = Column(String(254), unique=True)
