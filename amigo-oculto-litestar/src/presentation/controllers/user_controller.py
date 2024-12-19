from litestar import Controller, Request, get
from litestar.di import Provide

from infra.sqlalchemy.db import get_session
from infra.sqlalchemy.repositories.sqlalchemy_user_repository import (
    SQLAlchemyUserRepository,
)
from presentation.middlewares.auth_middleware import JWTAuthMiddleware


class UserController(Controller):
    dependencies = {
        "session": Provide(get_session),
        "user_repository": Provide(SQLAlchemyUserRepository, sync_to_thread=False),
    }

    @get("/me", middleware=[JWTAuthMiddleware])
    def me(request: Request) -> None:
        print(request.user)
