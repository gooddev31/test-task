from sqlalchemy import Column, String, Integer

from database.connection import Base, engine


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    description = Column(String)


Base.metadata.create_all(engine)
