from models.books import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.books import Book

engine = create_engine("sqlite:///data.db")

Session = sessionmaker(bind=engine)
session = Session()

users = [
    User(username="comicfan"),
    User(username="steveo"),
    User(username="davesteve"),
]

session.bulk_save_objects(users)
session.commit()


books = [Book(title="Spiderman"), Book(publisher="Marvel")]
session.bulk_save_objects(books)
session.commit()
