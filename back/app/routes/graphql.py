from flask_graphql import GraphQLView
from . import api_v1
from ..schemas import schema

# Essentially app.route but lower-level
api_v1.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        # graphiql=True,
    )
)
