from models import User, Book

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///data.db")

Session = sessionmaker(bind=engine)
session = Session()


users = [
    User(username="Dude"),
    User(username="Stevedave"),
    User(username= "Brodie"),
    User(username="Silent Bob"),
    User(username= "Jay"),
    User(username="Holden")
    User(username="Dante")
    User(username="Randall")
    User(username="Caitlyn Bre")
    User(username="Brad")
]

print(users)
session.bulk_save_objects(users)
session.commit()


session.query(User).delete()
session.commit()


comics = [
    Book(title="Black Panther", publisher="Marvel"),
    Book(title="Ironman", publisher="Marvel"),
    Book(title="Xmen", publisher="Marvel"),
    Book(title="XFactor", publisher="Marvel"),
    Book(title="New Mutants", publisher="Marvel"),
    Book(title="Spiderman", publisher="Marvel"),
    Book(title="Avengers", publisher="Marvel"),
    Book(title="Fantastic Four", publisher="Marvel"),
    Book(title="Thor", publisher="Marvel"),
    Book(title="Guardians of the Galaxy", publisher="Marvel"),
    Book(title="ShadowHawk", publisher="Image"),
    Book(title="Maxx", publisher="Image"),
    Book(title="Wet Works", publisher="Image"),
    Book(title="WildCats", publisher="Image"),
    Book(title="Cyberforce", publisher="Image"),
    Book(title="Walking Dead", publisher="Image"),
    Book(title="Spawn", publisher="Image"),
    Book(title="YoungBlood", publisher="Image"),
    Book(title="Savage Dragon", publisher="Image"),
    Book(title="Prophet", publisher="Image"),
    Book(title="Justice League", publisher="DC"),
    Book(title="Green Arrow", publisher="DC"),
    Book(title="Nightwing", publisher="DC"),
    Book(title="Flash", publisher="DC"),
    Book(title="Teen Titans", publisher="DC"),
    Book(title="Catwoman", publisher="DC"),
    Book(title="Aquaman", publisher="DC"),
    Book(title="Superman", publisher="DC"),
    Book(title="Batman", publisher="DC"),
    Book(title="Wonder Woman", publisher="DC"),
]

print(books)
session.bulk_save_objects(books)
session.commit()


session.query(Book).delete()
session.query(User).delete()
