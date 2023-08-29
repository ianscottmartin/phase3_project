##from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import declarative_base

#Base = declarative_base()

#class User(Base):
    #__tablename__ = 'user'
    
   # id = Column(Integer, primary_key=True)
    #username = Column(String)
    
    #def __repr__(self):
       # return f"\n<User"\
       #     +f"id{self.id},"\
        #    +f"username={self.username},"\
         #   +f"email={self.email},"\
          #  + ">"
            
#class Comic(Base):  
   # __tablename__ = 'comics'
    
   # id = Column(Integer, primary_key=True)
    #title= Column(String, Null=False)  
    #publisher= Column(String, Null=False)
    
    #def __repr__(self):
       # return f"\n<Comic"\
       #     +f"id{self.id},"\
       #     +f"publisher={self.publisher},"\
       #     +f"title{self.title}," 
            
 from sqlalchemy import Column, String, Integer, ForeignKey, relationship, Table



from .base import Base


#class UserComic(Base):
   # __tablename__ = "user_comic"

    #id = Column(Integer, String primary_key=True)
        

user_comics = Table(
    "user_comic",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user.id")),
    Column("comic_id", ForeignKey("comic.id")),
)
#make join table here
class Comic(Base):  
    __tablename__ = 'comic'
    
    id = Column(Integer, primary_key=True)
    title= Column(String, Null=False)  
    publisher= Column(String, Null=False)
    
    def __repr__(self):
        return f"\n<Comic"\
            +f"id{self.id},"\
            +f"publisher={self.publisher},"\
            +f"title{self.title}," 
users = relationship("User", secondary=user_comic)
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