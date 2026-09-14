from fastapi import Depends
from UserModule.Service.user_services import UserRepository, UserService
from global_dependencies import get_db

def get_user_service(db = Depends(get_db)):
    repository = UserRepository(db)
    service = UserService(repository)
    return service
    