from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__)

# Enforce mutations from sub-modules
from . import (
    graphql,
    hello,
)
