from fastapi import APIRouter, Depends, HTTPException
from BookModule.Schema.book_schemas import BookCreate, BookResponse
from BorrowModule.Schema.borrow_schemas import BorrowResponse
from BookModule.Service.book_services import BookService
from BookModule.Dependencies.book_depends import get_book_service


book_router = APIRouter(prefix="/Book",
                          tags=["Book"]      
                    )

@book_router.post("/create_book")
def create_book(book : BookCreate, service : BookService = Depends(get_book_service)):
      try:
            service.create_book(book.title, book.author, book.publication_year, book.available_copies)
            return {"Message" : "Livre crée avec succès"}
      except ValueError as e:
            raise HTTPException(status_code=404, detail=(e))

@book_router.get("/get_book_by_id/{book_id}", response_model=BookResponse)
def get_book_by_id(book_id : int, service : BookService = Depends(get_book_service)):
      return service.get_book_by_id(book_id)

@book_router.get("/get_all_book", response_model=list[BookResponse])
def get_all_book(service : BookService = Depends(get_book_service)):
      return service.get_all_book()

@book_router.get("/{book_id}/borrows", response_model = list[BorrowResponse])
def book_borrows(book_id : int, service : BookService = Depends(get_book_service)):
      return service.get_book_borrow(book_id)

