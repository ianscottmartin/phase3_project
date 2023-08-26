from models.books import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.books import Book

engine = create_engine("sqlite:///data.db")

Session = sessionmaker(bind=engine)
session = Session()

import random
from faker import Faker


for _ in range(10):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{first_name}_{last_name}@gmail.com"
    user = User(first_name=first_name, last_name=last_name, email=email, id=fake.id())


session.bulk_save_objects(users)
session.commit()


books = [
    Book(title="Black Panther"),
    Book(publisher="Marvel"),
    Book(title="Ironman"),
    Book(publisher="Marvel"),
    Book(title="Xmen"),
    Book(publisher="Marvel"),
    Book(title="XFactor"),
    Book(publisher="Marvel"),
    Book(title="New Mutants"),
    Book(publisher="Marvel"),
    Book(title="Amazing Spiderman"),
    Book(publisher="Marvel"),
    Book(title="Avengers"),
    Book(publisher="Marvel"),
    Book(title="Fantastic Four"),
    Book(publisher="Marvel"),
    Book(title="Thor"),
    Book(publisher="Marvel"),
    Book(title="Guardians of the Galaxy"),
    Book(publisher="Marvel"),
    Book(title="ShadowHawk"),
    Book(publisher="Image"),
    Book(title="Maxx"),
    Book(publisher="Image"),
    Book(title="Wet Works"),
    Book(publisher="Image"),
    Book(title="WildCats"),
    Book(publisher="Image"),
    Book(title="Cyberforce"),
    Book(publisher="Image"),
    Book(title="Walking Dead"),
    Book(publisher="Image"),
    Book(title="Spawn"),
    Book(publisher="Image"),
    Book(title="YoungBlood"),
    Book(publisher="Image"),
    Book(title="Savage Dragon"),
    Book(publisher="Image"),
    Book(title="Prophet"),
    Book(publisher="Image"),
    Book(title="Justice League"),
    Book(publisher="DC"),
    Book(title="Green Arrow"),
    Book(publisher="DC"),
    Book(title="Nightwing"),
    Book(publisher="DC"),
    Book(title="Flash"),
    Book(publisher="DC"),
    Book(title="Teen Titans"),
    Book(publisher="DC"),
    Book(title="Catwoman"),
    Book(publisher="DC"),
    Book(title="Aquaman"),
    Book(publisher="DC"),
    Book(title="Superman"),
    Book(publisher="DC"),
    Book(title="Batman"),
    Book(publisher="DC"),
    Book(title="Wonder Woman"),
    Book(publisher="DC"),
]

session.bulk_save_objects(books)
session.commit()
