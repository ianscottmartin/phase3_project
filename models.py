from sqlalchemy.orm import declarative_base
Base=declarative_base()

class User(Base):
    __tablename__ = "users"
    Column(id)