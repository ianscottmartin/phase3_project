from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
