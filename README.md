# phase3_project

# phase3 project Comic Selector app

# Project Blog https://medium.com/@ianscottmartin/setting-up-a-database-using-sqlalchemy-59856f77cd78

# video

OOP class for comic with attributes
class of User with attributes

Database Tables
use sqlalchemy
Table: Users
-id
-email
-name

Table: Comics
-id
-title
-publisher
-issue number

Table: association table between users and comics
-join table of relationship
-id
-user who liked it id

Type of relationship: one ot many user may have one or many to comics
comics can have a relationship of many to many between users
-relationships
-user_comic_liked
-user can many fav comics
Comic can be liked by many users
user to comics = many to many relationship
How ot use lists and dictionaries Use a list to show the relationships between users and comics

Aggregate methods to project
-CRUD
-Create- create list(join table)
-Read
-display all comics
-display liked comics

    -Update-
    -Delete remove from list of liked

show a list of comics a user has. or relationship of comic with users

-user can have a list of comics as id's-join table
dictionary: comic has a set of attributes and values

Users:
-many to many relationship with comics
-id:integer not null primary key
-email string not null, unique
-name string not null , unique

Comics
many to many relationship with users
-id integer not null unique primary key
-publisher string not null
-title string, integer

user liked comics

(join table)

-id integer not null primary key
-comic id integer not null
user who liked it id integer not null



# Catalogue comic books by publisher and user


# 1. create virtual environment- had to delete pipfile and pipfile.lock in main directory

# 2. install dependencies

    # a. SQLAlchemy 1.4.41

    # b. Alembic (migration manager)

    # c. ipdb as a debugger

    # d. faker-generate fake data

# 4. create the migration environment

# alembic init migrations

# 5. configure the migration environment (alembic.ini and env.py) finished

# 6. create declarative environment

# init

# 7. create schema python classes or models

# models.py, users.py, books.py

# 8. populate the database with seeds

# 9. test the environment relationships one to many


