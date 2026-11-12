from app.core.auth import create_access_token

token = create_access_token(
    {
        "sub": "priya@gmail.com"
    }
)

print(token)