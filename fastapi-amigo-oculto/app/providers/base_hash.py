class BaseHashProvider:
    def hash_password(self, senha: str) -> str:
        raise NotImplementedError
    def verify_password(password: str, hashed_password: str) -> bool:
        raise NotImplementedError