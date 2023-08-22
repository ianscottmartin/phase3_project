from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column("user_id", Integer, primary_key=True)
    username = Column("user_name", String, unique=True)
    email = Column(String(55))

    def __repr__(self):
        return (
            f"\n<User"
            + f"id={self.id}, "
            + f"username={self.username}, "
            + f"email={self.email}, "
            + f"created_at={self.create_at},"
            + f"updated_at={self.updated_at},"
            + ">"
        )
