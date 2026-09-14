from BorrowModule.Repository.borrow_repository import BorrowRepository
from BorrowModule.Model.borrow_model import Borrow
from UserModule.Repository.user_repository import UserRepository
from BookModule.Repository.book_repository import BookRepository
from BookModule.Model.book_model import Book
from UserModule.Model.user_model import User
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from global_dependencies import get_db


class BorrowService:
    
    def __init__(self, db : Session, borrowrepository : BorrowRepository, userrepository : UserRepository, bookrepository : BookRepository):
        self.borrowrepository = borrowrepository
        self.userrepository = userrepository
        self.bookrepository = bookrepository
        self.db = db
        
    def borrow_book(self, current_user_id : int , book_id : int) -> None :
            
            with self.db.begin():
                    current_user : User = self.userrepository.get_user_by_id(current_user_id)
                    book : Book = self.bookrepository.get_book_for_update(book_id)
    
                    if current_user is None:
                        raise HTTPException(status_code = 404, detail=str("Les informations renseignées sont invalides"))
    
                    if book is None :
                        raise HTTPException(status_code = 404, detail=str("Les informations renseignées sont invalides"))
    
                    if book.available_copies <= 0:
                        raise HTTPException(status_code = 409, detail=str("Le livre n'est plus en stock"))
    
                    existing_borrow = self.borrowrepository.get_existing_borrow(current_user.id, book.id)
    
                    if existing_borrow is not None:
                        raise HTTPException(status_code = 409, detail=str("Vous avez déjà empruntée ce livre"))    
    
                    borrow : Borrow = Borrow(user_id = current_user_id , book_id = book_id)
                    self.borrowrepository.create_borrow(borrow) 
                          
                    book.available_copies -= 1
    
    def return_book(self, current_user_id : int ,borrow_id : int, ): 
        
        borrow : Borrow = self.borrowrepository.get_borrow_by_id(borrow_id)
        if borrow is None:
            raise ValueError("Le livre emprunté n'existe pas")
        if current_user_id != borrow.user_id:
            raise ValueError("Vous ne possedez pas ce livre")
        book : Book = borrow.book
        if book is None:
            raise ValueError("Le livre emprunté n'existe pas")
        book.available_copies += 1
        self.bookrepository.update_book(book)
        self.borrowrepository.delete(borrow.id)
        
    
    def get_borrow_by_id(self, borrow_id : int):
        return self.borrowrepository.get_borrow_by_id(borrow_id)
    
    def get_all_borrows(self):
        return self.borrowrepository.get_all_borrow()                    