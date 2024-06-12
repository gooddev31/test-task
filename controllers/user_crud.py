from sqlalchemy.orm import Session

from database.models import Users
from schemas.user import *


def create_user(db: Session, user: CreateUser):
    db_user = Users(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, email: str, password: str) -> User:
    return db.query(Users).filter_by(email=email, password=password).one()
