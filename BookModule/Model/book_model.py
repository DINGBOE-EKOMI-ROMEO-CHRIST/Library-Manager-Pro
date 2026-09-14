from database_environnement import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    author = Column(String(50))
    publication_year = Column(Integer)
    available_copies = Column(Integer)
    borrows = relationship("Borrow", back_populates="book")
    