from BorrowModule.Model.borrow_model import Borrow

class BorrowRepository:
    
    def __init__(self, db):
        self.db = db
    
    def create_borrow(self, borrow : Borrow ):
        self.db.add(borrow)
        #self.db.commit()
        #self.db.refresh(borrow)
        return borrow
        
    def get_all_borrow(self):
        return self.db.query(Borrow).all()
    
    def get_borrow_by_id(self, borrow_id : int):
        borrow = self.db.query(Borrow).filter( Borrow.id == borrow_id ).first()
        if not borrow:
            raise ValueError("Emprunt introuvable")
        return borrow
    
    def delete(self, borrow_id : int):
        target_borrow = self.get_borrow_by_id(borrow_id)
        self.db.delete(target_borrow)
        self.db.commit()
    
    def get_existing_borrow(self, user_id, book_id):
        return self.db.query(Borrow).filter(Borrow.user_id == user_id, Borrow.book_id == book_id).first()
    
    