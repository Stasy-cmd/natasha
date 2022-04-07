from dao.models.base import BaseMixin
from setup_db import db


class User(BaseMixin, db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String)
    surname = db.Column(db.String)

    def __repr__(self):
        return f"<User '{self.email.title()}'>"
