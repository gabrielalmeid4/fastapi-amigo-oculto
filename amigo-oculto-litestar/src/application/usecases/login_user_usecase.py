from dataclasses import dataclass

from application.providers.hash_provider import HashProvider
from application.providers.token_provider import TokenProvider
from core.settings import settings
from domain.entities.user_entity import User
from domain.repositories import UserRepository
from presentation.exceptions.user_exceptions import (
    CredentialsException,
)


@dataclass
class LoginRequest:
    user_phone_number: str
    user_password: str


@dataclass
class LoginResponse:
    refresh_token: str
    access_token: str


class LoginUserUsecase:
    def __init__(
        self,
        user_repository: UserRepository,
        hash_provider: HashProvider,
        token_provider: TokenProvider,
    ):
        self.user_repository = user_repository
        self.hash_provider = hash_provider
        self.token_provider = token_provider

    async def execute(self, login_data: LoginRequest) -> LoginResponse:
        user_found: User = await self.user_repository.get_user_by_phone_number(
            login_data.user_phone_number,
        )

        if not user_found:
            raise CredentialsException()

        valid_login = self.hash_provider.verify(
            user_found.password, login_data.user_password
        )

        if not valid_login:
            print("Login não válido")
            raise CredentialsException()

        access_token = self.token_provider.encode(
            {"sub": user_found.phone_number},
            expires=settings.ACESS_TOKEN_EXPIRES_SECONDS,
        )

        refresh_token = self.token_provider.encode(
            {"sub": user_found.phone_number},
            expires=settings.ACESS_TOKEN_EXPIRES_SECONDS
            + settings.REFRESH_TOKEN_EXPIRES_SECONDS,
        )

        return LoginResponse(refresh_token, access_token)
