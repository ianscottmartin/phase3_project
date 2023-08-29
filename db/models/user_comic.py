from sqlalchemy import Column, String, Integer
from .base import Base


class UserComic(Base):
    __tablename__ = "user_comics"

    id = Column(Integer, String primary_key=True)
    pass

#make join table here
