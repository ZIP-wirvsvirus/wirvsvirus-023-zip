import time

from flask import current_app
from itsdangerous import URLSafeTimedSerializer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref

from .db import db


def timestamp():
    """Return the current timestamp as an integer."""
    return int(time.time())


class NewsEntry(db.Model):
    __tablename__ = 'news_entry'
    news_id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(120), index=True, unique=True)
    query_url = db.Column(db.String(128), nullable=False)
    created = db.Column(db.Integer, default=timestamp)
    last_update = db.Column(db.Integer, default=timestamp, onupdate=timestamp)
    content = db.Column(db.JSON)
    area = db.Column(db.String(128), nullable=True)
    category = db.Column(db.String, nullable=True)
    tags = db.Column(db.JSON)

    def as_dict(self):
        return dict((col, getattr(self, col)) for col in
                    self.__table__.columns.keys())