from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from jose import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


load_dotenv()


ACCESS_TOKEN_EXPIRY_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', '30')
ACCESS_TOKEN_SECRET_KEY = os.getenv('ACCESS_TOKEN_SECRET_KEY')
ACCESS_TOKEN_ALGORITHM = os.getenv('ACCESS_TOKEN_ALGORITHM', 'HS256')

# Validate required environment variables
if not ACCESS_TOKEN_SECRET_KEY:
    raise ValueError(
        "ACCESS_TOKEN_SECRET_KEY environment variable is not set. "
        "Please set it in your .env file."
    )


security = HTTPBearer()


class JWTGenerator:

    def create_access_token(self, data: dict, expires_at: timedelta | None = None):
        if not ACCESS_TOKEN_SECRET_KEY:
            raise ValueError("ACCESS_TOKEN_SECRET_KEY is not set. Cannot create token.")
            
        encoded_data = data.copy()
        if expires_at:
            expire = datetime.now() + expires_at
        else:
            expire = datetime.now() + \
                timedelta(minutes=float(ACCESS_TOKEN_EXPIRY_MINUTES))

        encoded_data['exp'] = expire
        return jwt.encode(
            encoded_data,
            ACCESS_TOKEN_SECRET_KEY,
            algorithm=ACCESS_TOKEN_ALGORITHM,
        )

    def decode_access_token(self, token: str) -> dict:
        if not ACCESS_TOKEN_SECRET_KEY:
            raise HTTPException(
                status_code=500, 
                detail="JWT secret key not configured"
            )
        
        if not token:
            raise HTTPException(status_code=401, detail="Token is required")
            
        try:
            payload = jwt.decode(
                token,
                ACCESS_TOKEN_SECRET_KEY,
                algorithms=[ACCESS_TOKEN_ALGORITHM]  # Must be a list
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.JWTError as e:
            # More specific error message for debugging
            error_msg = str(e)
            if "Invalid crypto padding" in error_msg or "Invalid token" in error_msg:
                raise HTTPException(
                    status_code=401, 
                    detail="Invalid token. This may be due to a mismatched secret key or corrupted token."
                )
            raise HTTPException(status_code=401, detail=f"Invalid token: {error_msg}")

    def handle_token_authorization(self, credentials: HTTPAuthorizationCredentials = Security(security)):
        token = credentials.credentials
        return self.decode_access_token(token)


jwt_generator: JWTGenerator = JWTGenerator()
