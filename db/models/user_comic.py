from sqlalchemy import Column, String, Integer, ForeignKey, relationship


from .base import Base


class UserComic(Base):
    __tablename__ = "user_comics"

    id = Column(Integer, String primary_key=True)
    pass

user_comics = Table(
    "user_comics",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user.id")),
    Column("comic_id", ForeignKey("comic.id")),
)
#make join table here
