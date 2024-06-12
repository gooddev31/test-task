from sqlalchemy.orm import Session

from database.models import Posts
from schemas.posts import DeletePostResponse, Post, UpdatePost


def post_create(db: Session, post: Post):
    db_post = Posts(text=post.text, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def posts_get_all(db: Session):
    return db.query(Posts).all()

def get_user_posts(db: Session, user_id: int):
    return db.query(Posts).filter_by(user_id=user_id)


def post_get_one(db: Session, id: int):
    return db.query(Posts).filter_by(id=id).one()


def post_update(db: Session, post: UpdatePost):
    update_query = {Posts.title: post.text}
    db.query(Posts).filter_by(id=post.id).update(update_query)
    db.commit()
    return db.query(Posts).filter_by(id=post.id).one()


def post_delete(db: Session, id: int):
    post = db.query(Posts).filter_by(id=id).all()
    if not post:
        return DeletePostResponse(detail="Doesnt Exist")
    db.query(Posts).filter_by(id=id).delete()
    db.commit()
    return DeletePostResponse(detail="Post Deleted")
