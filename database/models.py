import time
from .db import db


def timestamp():
    """Return the current timestamp as an integer."""
    return int(time.time())


class NewsEntry(db.Model):
    __tablename__ = 'news_entry'
    identifier = db.Column(db.String(128), primary_key=True, unique=True)
    source = db.Column(db.String(128))
    query_url = db.Column(db.String(128), nullable=False)
    created = db.Column(db.DateTime, default=timestamp)
    last_update = db.Column(db.DateTime, default=timestamp, onupdate=timestamp)
    content = db.Column(db.String(8192))
    headline = db.Column(db.String(1024))
    area = db.Column(db.String(128), nullable=True)
    category = db.Column(db.String, nullable=True)
    tags = db.Column(db.JSON)

    @staticmethod
    def serialize(ob):
        return {'source': ob.source, 'query_url': ob.query_url, 'created': ob.created,
                'last_update': ob.last_update, 'headline': ob.headline, 'content': ob.content, 'area': ob.area,
                'category': ob.category, 'tags': ob.tags}

    def as_dict(self):
        return dict((col, getattr(self, col)) for col in
                    self.__table__.columns.keys())
