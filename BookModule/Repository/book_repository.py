from BookModule.Model.book_model import Book
from global_dependencies import get_db
from fastapi import Depends

class BookRepository:
    
    def __init__(self, db):
        self.db = db
        
    
    def create_book(self, book : Book):
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
    
    def get_all_books(self):
        return self.db.query(Book).all()
    
    def get_book_by_id(self, book_id : int):
        book = self.db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise ValueError("Le livre est introuvable")
        return book
    
    def update_book(self, book : Book):
        self.db.commit()
        self.db.refresh(book)
    
    def get_book_for_update(self, book_id : int):
        return self.db.query(Book).filter(Book.id == book_id).with_for_update().first()