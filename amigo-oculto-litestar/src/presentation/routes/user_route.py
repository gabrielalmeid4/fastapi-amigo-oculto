from litestar import Router

from presentation.controllers.user_controller import UserController

user_route = Router(
    path="/users",
    route_handlers=[UserController],
)
