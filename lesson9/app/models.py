# в app/models.py
# теперь опишем простую таблицу
from datetime import datetime

from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, unique=True)
    created = db.Column(db.DateTime(), default=datetime.utcnow)
    text = db.Column(db.Text())

    def __repr__(self):
        return '<Post {}>'.format(self.title)