import bcrypt
from bcrypt import checkpw, hashpw

from application.providers.hash_provider import HashProvider


class BCryptHashProvider(HashProvider):
    def hash(self, payload: str) -> str:
        bytes_payload = payload.encode("utf-8")
        return hashpw(bytes_payload, bcrypt.gensalt()).decode("utf-8")

    def verify(self, hashed: str, payload: str) -> bool:
        hashed = str(hashed)
        bytes_payload = payload.encode("utf-8")
        bytes_hashed = hashed.encode("utf-8")
        return checkpw(bytes_payload, bytes_hashed)
