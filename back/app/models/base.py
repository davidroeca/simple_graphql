from .database import db

class Base(db.Model):
    '''Define base as subclass of db.Model for flexibility'''
    __abstract__ = True
