from alchemy_repositories import db
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    created = db.Column(db.DateTime(), default=datetime.utcnow())
    title = db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)