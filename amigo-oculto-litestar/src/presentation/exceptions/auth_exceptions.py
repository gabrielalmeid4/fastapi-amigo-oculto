from litestar import status_codes as status

from presentation.exceptions.base_exceptions import AppError


class UnauthorizedCredentialsException(AppError):
    def __init__(
        self,
        message="Credenciais inválidas",
        status_code=status.HTTP_401_UNAUTHORIZED,
    ):
        super().__init__(message, status_code)


class TokenExpiredException(UnauthorizedCredentialsException):
    def __init__(
        self,
        message="Credenciais inválidas",
        status_code=status.HTTP_401_UNAUTHORIZED,
    ):
        super().__init__(message, status_code)
