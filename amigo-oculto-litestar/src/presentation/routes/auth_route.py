from litestar import Router

from presentation.controllers.auth_controller import AuthController

auth_route = Router(
    path="/auth",
    route_handlers=[AuthController],
)
