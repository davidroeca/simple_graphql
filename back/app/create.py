from typing import Dict, Any
from flask import Flask
from flask_cors import CORS
from .models.base import Base
from .models import db
from .routes import api_v1

def create_app(config: Dict[str, Any]):
    app = Flask(__name__)
    app.config.update(config)
    db.init_app(app)
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    with app.app_context():
        db.drop_all()
        db.create_all()
        from .models import User, Post
        joe = User(
            display_name='Joe',
            username='jomama',
            email='joe@hotmail.com',
        )
        hey = Post(
            subject='Hey',
            body='First post here, sup yall!',
            author=joe,
        )
        yo = Post(
            subject='Heyo',
            body='Yo yo second post, peace out homies',
            author=joe,
        )
        sandy = User(
            username='sandy',
            email='sandy@gmail.com',
        )
        db.session.add(hey)
        db.session.add(yo)
        db.session.add(sandy)
        db.session.commit()
    CORS(app)
    return app
