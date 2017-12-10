'''GraphQL Schemas'''

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

from .. import models
from ..models import db
from .data import User, Post
from .form import (
    FormState,
    FormSection,
    FormField,
    FormFieldSelectOption,
    Submission,
)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    posts = SQLAlchemyConnectionField(Post)
    users = SQLAlchemyConnectionField(User)
    form_state = graphene.Field(FormState)

    def resolve_form_state(self, info):
        subject_field = FormField(
            name='Subject',
            field_name='subject',
        )
        body_field = FormField(
            name='Please write post',
            field_name='body',
        )
        author_field = FormField(
            name='Author',
            field_name='author_email',
            options=[
                FormFieldSelectOption(
                    label=(
                        u.display_name
                        if u.display_name is not None else
                        u.username
                    ),
                    value=u.email
                )
                for u in db.session.query(models.User)
            ],
        )
        primary_section = FormSection(
            name='primary',
            fields=[
                body_field,
                subject_field,
                author_field,
            ]
        )
        return FormState(
            sections=[primary_section]
        )

class Mutations(graphene.ObjectType):
    submission = Submission.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
