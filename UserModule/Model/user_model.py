from database_environnement import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    email = Column(String(50), unique=True)
    password = Column(String(255))
    borrows = relationship("Borrow", back_populates="user")