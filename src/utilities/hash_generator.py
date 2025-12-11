
from passlib.hash import bcrypt_sha256
import hashlib
import bcrypt


class HashGenerator:
    def hash_password(self, password: str) -> str:
        hashed = hashlib.sha256(password.encode()).digest()
        return bcrypt.hashpw(hashed, bcrypt.gensalt())

    def verify_hash_password(
        self,
        password: str,
        hashed_password: str
    ) -> bool:
        hashed = hashlib.sha256(password.encode()).digest()
        return bcrypt.checkpw(hashed, hashed_password)


hash_generator: HashGenerator = HashGenerator()
