from cw.config import DevelopmentConfig
from cw import *  # noqa F401, F403
from cw.server import create_app
from cw.setup_db import db

app = create_app(DevelopmentConfig)

with app.app_context():
    db.drop_all()
    db.create_all()
