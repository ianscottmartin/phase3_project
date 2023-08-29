##from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import declarative_base

#Base = declarative_base()

#class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    
    def __repr__(self):
        return f"\n<User"\
            +f"id{self.id},"\
            +f"username={self.username},"\
            +f"email={self.email},"\
            + ">"
            
#class Book(Base):  
   # __tablename__ = 'book'
    
   # id = Column(Integer, primary_key=True)
    #title= Column(String, Null=False)  
    #publisher= Column(String, Null=False)
    
    #def __repr__(self):
       # return f"\n<Book"\
       #     +f"id{self.id},"\
       #     +f"publisher={self.publisher},"\
       #     +f"title{self.title}," 
            
            