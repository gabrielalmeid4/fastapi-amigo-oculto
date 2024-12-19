from datetime import datetime, timedelta

class BaseTokenProvider:
    def create_token(data: dict, SECRET_KEY: str, ALGORITHM: str, expires_delta: timedelta = None):
        raise NotImplementedError
    def verify_token(token: str, SECRET_KEY: str, ALGORITHM: str):
        raise NotImplementedError