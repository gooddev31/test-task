from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base, engine

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String)
    password = Column(String)

    posts = relationship("Posts", back_populates="user")

class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("Users", back_populates="posts")


Base.metadata.create_all(engine)
