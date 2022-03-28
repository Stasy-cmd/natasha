from cw.dao.models.base import BaseMixin
from cw.setup_db import db


class Director(BaseMixin, db.Model):
    __tablename__ = "directors"
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Director '{self.name.title()}'>"
