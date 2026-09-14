from database_environnement import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Borrow(Base):
    __tablename__ = "borrows"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    
    user = relationship("User", back_populates="borrows")
    book = relationship("Book", back_populates="borrows")
    
    borrow_date = Column(DateTime(timezone=True))
    
    