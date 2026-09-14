from fastapi import Depends
from BookModule.Service.book_services import BookRepository, BookService
from global_dependencies import get_db

def get_book_service(db = Depends(get_db)):
    repository = BookRepository(db)
    service = BookService(repository)
    return service