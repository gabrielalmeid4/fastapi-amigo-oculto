from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///database.db"
    TOKEN_ALGORITHM: str = "HS256"
    TOKEN_SECRET: str = "LAgAUHhaUZoghqXgwu+Kqg=="
    ACESS_TOKEN_EXPIRES_SECONDS: int = 9999
    REFRESH_TOKEN_EXPIRES_SECONDS: int = 99999


settings = Settings()
