from UserModule.Repository.user_repository import UserRepository
from UserModule.Model.user_model import User

class UserService:
    
    def __init__(self, userrepository : UserRepository):
        self.userrepository = userrepository
    
    def get_user_borrow(self, user_id : int):
        target_user : User = self.userrepository.get_user_by_id(user_id)
        return target_user.borrows
    
    def create_user(self, username : str, email : str):
        user : User = User(username = username, email = email)
        self.userrepository.create_user(user)
        
    def get_user_by_id(self, user_id : int):
        return self.userrepository.get_user_by_id(user_id)

    def get_all_user(self):
        return self.userrepository.get_all_user()
    
    def get_user_by_username(self, username : str):
        user = self.get_user_by_username(username)
        if user is None:
            raise ValueError("Identifiant Invalide")
        return user
    
    def get_user_by_email(self, email : str):
        return (self.userrepository.get_user_by_email(email.strip()))
    