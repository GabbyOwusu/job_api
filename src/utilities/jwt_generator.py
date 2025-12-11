from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from jose import jwt

load_dotenv()


ACCESS_TOKEN_EXPIRY_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
ACCESS_TOKEN_SECRET_KEY = os.getenv('ACCESS_TOKEN_SECRET_KEY')
ACCESS_TOKEN_ALGORITHM = os.getenv('ACCESS_TOKEN_ALGORITHM')


class JWTGenerator:

    def create_access_token(self, data: dict, expires_at: timedelta | None = None):
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

    def decode_access_token(token: str) -> int | None:
        payload = jwt.decode(
            token,
            ACCESS_TOKEN_SECRET_KEY,
            algorithms=ACCESS_TOKEN_ALGORITHM
        )
        return payload['user_id']


jwt_generator: JWTGenerator = JWTGenerator()
