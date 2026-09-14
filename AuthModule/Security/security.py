from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated = "auto"
)

key = "super_secret_key"
algorithm="HS256"


def hash_password(password : str) -> str :
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password : str)-> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data : dict):
    payload = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=30)

    payload.update(
        {"exp" : expire}
    )
    
    return jwt.encode(
        payload, key, algorithm="HS256"
    )
    
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl='/auth/login'
)