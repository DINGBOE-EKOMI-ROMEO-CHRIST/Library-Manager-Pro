from global_dependencies import get_db
from fastapi import Depends
from AuthModule.Service.auth_services import AuthService
from UserModule.Repository.user_repository import UserRepository

def get_auth_service(db = Depends(get_db)):
    repo = UserRepository(db)
    service = AuthService(repo)
    return service