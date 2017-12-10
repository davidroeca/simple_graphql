import os
from app.create import create_app

PATH_HERE = os.path.dirname(os.path.realpath(__file__))
PATH_INSTANCE = os.path.join(PATH_HERE, 'instance')
PATH_DB = os.path.join(PATH_INSTANCE, 'app.db')

CONFIG = {
    'SQLALCHEMY_DATABASE_URI': f'sqlite:///{PATH_DB}',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'DEBUG': True,
}
APP = create_app(CONFIG)

if __name__ == "__main__":
    APP.run()
