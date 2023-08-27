from sqlalchemy import Column, Integer, String, ForeignKey, Table


user_books = Table(
    "user_books",
    Base.metadata,
    Column(Integer, primary_key=True),
    Column("user_id", ForeignKey("user_id")),
    Column("book_id", ForeignKey("book_id")),
    
) 

books = relationship("Book", secondary=user_books, backref="the_books")
