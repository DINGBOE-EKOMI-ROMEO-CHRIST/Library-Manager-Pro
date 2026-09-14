from UserModule.Model.user_model import User

class UserRepository:
    
    def __init__(self, db):
        self.db = db
        
    def create_user(self, user : User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
    
    def get_all_user(self):
        return self.db.query(User).all()
    
    def get_user_by_id(self, user_id : int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user :
            raise ValueError("L'utilisateur est introuvable")
        return user
    
    def get_user_by_username(self, username : str):
        user : User  = self.db.query(User).filter(User.username == username).first()
        return user
    
    def get_user_by_email(self, email : str):
        return (self.db.query(User).filter(User.email == email.strip()).first())
         
    
    
        