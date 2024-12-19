from http.client import HTTPException
from litestar import Litestar, Request, Response
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin, YamlRenderPlugin

from infra.sqlalchemy.db import create_tables
from presentation.exceptions.base_exceptions import AppError
from presentation.routes.auth_route import auth_route
from presentation.routes.user_route import user_route


def app_exception_handler(request: Request, exc: AppError) -> Response:
    return Response(
        content={
            "error_code": exc.code,
            "path": request.url.path,
            "detail": exc.detail,
            "status_code": exc.status_code,
        },
        status_code=exc.status_code,
    )


app = Litestar(
    route_handlers=[auth_route, user_route],
    on_startup=[create_tables],
    on_shutdown=[],
    openapi_config=OpenAPIConfig(
        title="HiddenFriendAPI",
        version="1.0.0",
        root_schema_site="swagger",
        render_plugins=[
            SwaggerRenderPlugin(path="/docs"),
            YamlRenderPlugin(path="/spec"),
        ],
    ),
    exception_handlers={AppError: app_exception_handler},
)

app.add_exception_handler()


UserNotFoundException = HTTPException(status=404, m)