from sqlalchemy import update
from app import app
from flask_sqlalchemy import SQLAlchemy
from models import Post

db = SQLAlchemy(app)
db.session.create_all()

def get_post(post_id):
    return Post.query.get(post_id)


def get_all_posts():
    return Post.query.all()


def add_post(title, content):
    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()


def update_post(title, content, id):
    db.session.execute(update(Post)
                       .where(Post.id == id)
                       .values(title=title, content=content))
    db.session.commit()


def delete_post(id):
    Post.query.filter_by(id=id).delete()
    db.session.commit()


def add_user(name, email, password):
    pass
