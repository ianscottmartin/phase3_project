from sqlalchemy import Column, Integer, String, ForeignKey, Table

        
class Book(Base):  
    __tablename__ = 'book'
    
    id = Column(Integer, primary_key=True)
    title= Column(String)  
    publisher= Column(String)
    
    def __repr__(self):
        return f"\n<Book"\
            +f"id{self.id},"\
            +f"publisher={self.publisher},"\
            +f"title{self.title}," 
            
            