from fastapi import APIRouter
from AuthModule.Schema.auth_schema import LoginRequest, RegisterRequest, TokenResponse
from AuthModule.Dependencies.auth_depends import get_auth_service
from AuthModule.Service.auth_services import AuthService
from fastapi import Depends, HTTPException

auth_router = APIRouter(prefix="/auth", tags=["authenticate"])


@auth_router.post("/register")
def register(user : RegisterRequest, service : AuthService = Depends(get_auth_service)):
    try:
        service.register(user.username, user.email, user.password)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    else:
        return {"message" : "Utilisateur crée avec succès"}


@auth_router.post("/login", response_model=TokenResponse, status_code = 200)
def login(user : LoginRequest, service : AuthService = Depends(get_auth_service)):
    try:
        token_response = service.login(user.username, user.password)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    else: 
        return token_response