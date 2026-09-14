from fastapi import APIRouter, Depends, HTTPException
from BorrowModule.Schema.borrow_schemas import BorrowCreate, BorrowResponse
from BorrowModule.Dependencies.borrow_depends import get_borrow_service
from BorrowModule.Service.borrow_services import BorrowService
from BorrowModule.Model.borrow_model import Borrow
from AuthModule.Dependencies.get_current_user import get_current_user
from UserModule.Model.user_model import User
borrow_router = APIRouter(prefix="/Borrow",
                          tags=["Borrow"]      
                    )

@borrow_router.post("/create_borrow")
def borrow_book(borrow : BorrowCreate, current_user : User = Depends(get_current_user), service : BorrowService = Depends(get_borrow_service)):
      try:
            service.borrow_book(current_user.id, borrow.book_id)
            return {"Message" : "L'emprunt a été crée avec succès"}
      except ValueError as e:
            raise HTTPException(status_code=404, detail=(e))

@borrow_router.get("/get_borrow_by_id/{borrow_id}", response_model=BorrowResponse)
def get_borrow_by_id(borrow_id : int, service : BorrowService = Depends(get_borrow_service)):
      return service.get_borrow_by_id(borrow_id)

@borrow_router.get("/get_all_borrows", response_model=list[BorrowResponse])
def get_all_borrows(service : BorrowService = Depends(get_borrow_service)):
      return service.get_all_borrows()

@borrow_router.post("/return_book/{borrow_id}")
def return_book(borrow_id : int, current_user : User = Depends(get_current_user),service : BorrowService = Depends(get_borrow_service)):
      try: 
            service.return_book(current_user.id, borrow_id)
            return {"Message" : "Livre rendu avec succès"}
      except ValueError as e:
            raise HTTPException(status_code=404, detail=e)