from fastapi import APIRouter, Depends, HTTPException
from UserModule.Schema.user_schemas import UserCreate, UserResponse
from BorrowModule.Schema.borrow_schemas import BorrowResponse
from UserModule.Dependencies.user_depends import get_user_service
from UserModule.Service.user_services import UserService
from UserModule.Model.user_model import User
from AuthModule.Dependenties.get_current_user import get_current_user

user_router = APIRouter(prefix="/User",
                        tags = ["User"]
                        )

@user_router.post("/create_user")
def create_user(user : UserCreate, service : UserService = Depends(get_user_service)):
    try:
        service.create_user(user.username, user.email)
        return {"Utilisateur" : user.username, "Message" : "Utilisateur crée avec succès"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=(e))

@user_router.get("/get_user_by_id/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id : int, service : UserService = Depends(get_user_service)):
    target_user = service.get_user_by_id(user_id)
    return target_user

@user_router.get("/{user_id}/borrows", response_model = list[BorrowResponse])
def user_borrows(user_id : int, service : UserService = Depends(get_user_service)):
    return service.get_user_borrow(user_id)
   
@user_router.get("/get_all_user", response_model=list[UserResponse])
def get_all_user(service : UserService = Depends(get_user_service)):
    return service.get_all_user()
    
@user_router.get("/me", response_model=UserResponse)
def me(current_user : User = Depends(get_current_user)):
    return current_user