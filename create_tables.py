
#from cw import *  # noqa F401, F403
from server import create_app
from setup_db import db

from config import DevelopmentConfig

app = create_app(DevelopmentConfig)

with app.app_context():
    db.drop_all()
    db.create_all()
