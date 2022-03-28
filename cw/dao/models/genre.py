from cw.dao.models.base import BaseMixin
from cw.setup_db import db


class Genre(BaseMixin, db.Model):
    __tablename__ = "genres"
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Genre '{self.name.title()}'>"
