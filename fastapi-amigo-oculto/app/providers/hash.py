import bcrypt
from app.providers.base_hash import BaseHashProvider

class HashProviderBCrypt(BaseHashProvider):
    async def hash_password(self, senha: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(senha.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    def verify_password(senha: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(senha.encode('utf-8'), hashed_password.encode('utf-8'))