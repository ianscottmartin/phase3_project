from sqlalchemy import Column, Integer, ForeignKey, String, relationship

from .base import Base

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(55), unique=True)
    email = Column(String(55))
    
    def __repr__(self):
        return f"\n<User"\
            +f"id{self.id},"\
            +f"username={self.username},"\
            +f"email={self.email},"\
            + ">"

comics= relationship("Comic", secondary=user_comic) 

    