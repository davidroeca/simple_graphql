'''Define all graphql interaces related to a front-end form'''

import graphene

from ..models import db
from .. import models
from .data import User

class FormFieldSelectOption(graphene.ObjectType):
    label = graphene.String()
    value = graphene.String(required=True)

class FormField(graphene.ObjectType):
    # Name used to display in form
    name = graphene.String()

    # Named used while making mutation
    field_name = graphene.String()

    options = graphene.List(FormFieldSelectOption)

class FormSection(graphene.ObjectType):
    name = graphene.String(required=True)
    fields = graphene.List(FormField, required=True)

class FormState(graphene.ObjectType):
    sections = graphene.List(FormSection)

class Submission(graphene.Mutation):
    class Arguments:
        subject = graphene.String(required=True)
        body = graphene.String(required=True)
        author_email = graphene.String(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, subject=None, body=None, author_email=None):
        author = db.session.query(models.User)\
            .filter_by(email=author_email)\
            .first()
        if not author:
            return cls(ok=False)
        new_post = models.Post(
            subject=subject,
            body=body,
            author=author,
        )
        db.session.add(new_post)
        db.session.commit()
        return Submission(ok=True)
