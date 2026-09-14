from BookModule.Repository.book_repository import BookRepository
from BookModule.Model.book_model import Book

class BookService:
    
    def __init__(self, bookrepository : BookRepository):
        self.bookrepository = bookrepository
        
    def get_book_borrow(self, book_id : int):
        target_book : Book = self.bookrepository.get_book_by_id(book_id)
        return target_book.borrows
    
    def create_book(self, title : str, author : str, publication_year : int, available_copies : int):
        book : Book = Book(title = title, author = author, publication_year = publication_year, available_copies = available_copies)
        self.bookrepository.create_book(book)
        
    def get_book_by_id(self, book_id):
        return self.bookrepository.get_book_by_id(book_id)
    
    def get_all_book(self):
        return self.bookrepository.get_all_books()