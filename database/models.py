import time
from .db import db


def timestamp():
    """Return the current timestamp as an integer."""
    return int(time.time())


class NewsEntry(db.Model):
    __tablename__ = 'news_entry'
    news_id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(128), nullable=True)
    source = db.Column(db.String(128))
    query_url = db.Column(db.String(128), nullable=False)
    created = db.Column(db.Integer, default=timestamp)
    last_update = db.Column(db.Integer, default=timestamp, onupdate=timestamp)
    content = db.Column(db.JSON)
    area = db.Column(db.String(128), nullable=True)
    category = db.Column(db.String, nullable=True)
    tags = db.Column(db.JSON)

    @staticmethod
    def serialize(ob):
        return {'id': ob.news_id, 'source': ob.source, 'query_url': ob.query_url, 'created': ob.created,
                'last_update': ob.last_update, 'content': ob.content, 'area': ob.area, 'category': ob.category,
                'tags': ob.tags}

    def as_dict(self):
        return dict((col, getattr(self, col)) for col in
                    self.__table__.columns.keys())
