from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from .. import models

class User(SQLAlchemyObjectType):
    '''User graphql interface'''
    class Meta:
        model = models.User
        interfaces = (relay.Node, )

class Post(SQLAlchemyObjectType):
    '''Post graphql interface'''
    class Meta:
        model = models.Post
        interfaces = (relay.Node, )
