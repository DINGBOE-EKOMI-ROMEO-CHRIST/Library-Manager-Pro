from pydantic import BaseModel

class BorrowCreate(BaseModel):
    book_id : int
    
class BorrowResponse(BaseModel):
    id : int
    user_id : int 
    book_id : int
   
class BorrowReturn(BaseModel):
    borrow_id : int