from UserModule.Repository.user_repository import UserRepository
from AuthModule.Security.security import create_access_token, verify_password, hash_password
from UserModule.Model.user_model import User

class AuthService:
    
    def __init__(self, user_repository : UserRepository):
        self.user_repository = user_repository
        
    def login(self, username : str, password : str):
        username = username.strip()
        password = password.strip()
        
        if not all([username, password]):
            raise ValueError("Les informations sont invalides")
        
        user = self.user_repository.get_user_by_username(username)
        
        if not user:
            raise ValueError("Les information sont invalides")
        
        if not verify_password(password, user.password):
            raise ValueError("Les informations sont invalides")
             
        access_token = create_access_token(
            {
                "sub" : user.username, 
                "user_id" : user.id
            }
        )
         
        return {
            "access_token" : access_token,
            "token_type" : "bearer"
        }
    
    
    def register(self, username : str, email : str, password : str):
        username = username.strip()
        email = email.strip()
        password = password.strip()
        
        if not all([username, password, email]):
            raise ValueError("Information Invalide...")
        
        target_user = self.user_repository.get_user_by_username(username)
        
        if target_user:
            raise ValueError("Le nom d'utilisateur existe déjà")
        if self.user_repository.get_user_by_email(email):
            raise ValueError("L'email existe déjà")
        
        hash_password = hash_password(password)
        
        user = User(username = username, 
                    email = email, 
                    password = hash_password
                    )
        
        self.user_repository.create_user(user)
        return user
        
        
        
        