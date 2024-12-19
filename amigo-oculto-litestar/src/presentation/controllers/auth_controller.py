from litestar import Controller, Request, post
from litestar.di import Provide

from application.providers.hash_provider import HashProvider
from application.providers.token_provider import TokenProvider
from application.usecases.login_user_usecase import LoginRequest, LoginUserUsecase
from application.usecases.register_user_usecase import RegisterRequest, RegisterUsecase
from domain.repositories.user_repository import UserRepository
from infra.providers.bcrypthash_provider import BCryptHashProvider
from infra.providers.josetoken_provider import JoseTokenProvider
from infra.sqlalchemy.db import get_session
from infra.sqlalchemy.repositories.sqlalchemy_user_repository import (
    SQLAlchemyUserRepository,
)
from presentation.middlewares.auth_middleware import JWTAuthMiddleware
from presentation.schemas.auth_schemas import AuthResponseSchema
from presentation.schemas.user_schemas import (
    UserLoginSchema,
    UserResponseSchema,
    UserSignupSchema,
)


class AuthController(Controller):
    dependencies = {
        "session": Provide(get_session),
        "user_repository": Provide(SQLAlchemyUserRepository, sync_to_thread=False),
        "token_provider": Provide(JoseTokenProvider, sync_to_thread=False),
        "hash_provider": Provide(BCryptHashProvider, sync_to_thread=False),
    }

    @post("/login")
    async def login(
        self,
        data: UserLoginSchema,
        request: Request,
        user_repository: UserRepository,
        hash_provider: HashProvider,
        token_provider: TokenProvider,
    ) -> AuthResponseSchema:
        usecase = LoginUserUsecase(user_repository, hash_provider, token_provider)

        login_response = await usecase.execute(
            LoginRequest(
                user_password=data.password,
                user_phone_number=data.phone_number,
            )
        )

        return AuthResponseSchema(**login_response.__dict__)

    @post("/register")
    async def register(
        self,
        data: UserSignupSchema,
        user_repository: UserRepository,
        hash_provider: HashProvider,
    ) -> UserResponseSchema:
        usecase = RegisterUsecase(user_repository, hash_provider)

        print(user_repository.session)

        register_response = await usecase.execute(RegisterRequest(**data.model_dump()))

        return UserResponseSchema(**register_response.user_created.__dict__)
