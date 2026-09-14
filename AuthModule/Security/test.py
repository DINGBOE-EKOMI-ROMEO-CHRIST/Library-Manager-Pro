from AuthModule.Security.security import (
    create_access_token
)

token = create_access_token(
    {
        "sub": "romeo",
        "user_id": 1
    }
)

print(token)