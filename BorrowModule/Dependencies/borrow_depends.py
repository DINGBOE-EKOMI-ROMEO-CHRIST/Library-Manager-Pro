from fastapi import Depends
from BorrowModule.Service.borrow_services import BorrowRepository, BorrowService
from BookModule.Service.book_services import BookRepository
from UserModule.Service.user_services import UserRepository
from global_dependencies import get_db

def get_borrow_service(db = Depends(get_db)):
    borrowrepository = BorrowRepository(db)
    userrepository = UserRepository(db)
    bookrepository = BookRepository(db)
    service = BorrowService(borrowrepository, userrepository, bookrepository)
    return service

