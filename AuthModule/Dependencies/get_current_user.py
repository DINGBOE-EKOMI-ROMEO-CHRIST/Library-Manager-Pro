from fastapi import Depends, HTTPException
from UserModule.Dependencies.user_depends import get_user_service
from UserModule.Service.user_services import UserService
from AuthModule.Security.security import oauth2_scheme, key, algorithm
from jose.exceptions import JWTError
from jose import jwt

def get_current_user(token : str = Depends(oauth2_scheme),  user_service : UserService = Depends(get_user_service)):
    try : 
        payload : dict = jwt.decode(token, key, algorithms = [algorithm])
    except JWTError:
        raise HTTPException(status_code=401, detail=("Unauthorized"))
    
    user_id = payload.get("user_id")
    
    user = user_service.get_user_by_id(user_id)
    
    if user is None:
        raise HTTPException(status_code=401, detail="Utilisateur non authentifié")
    
    return user
    
    