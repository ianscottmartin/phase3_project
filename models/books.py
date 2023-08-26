from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationships
from .session import session
from .base import Base




Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column("book_id", Integer, primary_key=True)
    title = Column("book_title", String, unique=True)
    publisher = Column(String(55))
    
    
    

    def __repr__(self):
        return (
            f"\n<Book"
            + f"id={self.id}, "
            + f"publisher={self.publisher}, "
            + f"title={self.title}, "
            + f"created_at={self.create_at},"
            + f"updated_at={self.updated_at},"
            + ">"
        )
