from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import relationship
#from .session import session
from .base import Base


class Comic(Base):  
    __tablename__ = 'comics'
    
    id = Column(Integer, primary_key=True)
    title= Column(String, Null=False)  
    publisher= Column(String, Null=False)
    
    def __repr__(self):
        return f"\n<Comic"\
            +f"id{self.id},"\
            +f"publisher={self.publisher},"\
            +f"title{self.title}," 
            