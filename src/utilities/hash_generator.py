import hashlib
import bcrypt


class HashGenerator:
    def hash_password(self, password: str) -> str:
        hashed = hashlib.sha256(password.encode()).digest()
        bcrypt_hash_bytes = bcrypt.hashpw(hashed, bcrypt.gensalt())
        return bcrypt_hash_bytes.decode('latin1')

    def verify_hash_password(self, password: str, hashed_password: str) -> bool:
        try:
            hashed = hashlib.sha256(password.encode()).digest()
            hashed_password_bytes = bytes.fromhex(hashed_password[2:])
            return bcrypt.checkpw(hashed, hashed_password_bytes)
        except:
            raise


hash_generator: HashGenerator = HashGenerator()
