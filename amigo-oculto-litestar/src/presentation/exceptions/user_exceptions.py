from litestar import status_codes as status

from presentation.exceptions.base_exceptions import AppError


class UserNotFoundException(AppError):
    def __init__(
        self,
        message="Usuário requisitado não encontrado",
        status_code=status.HTTP_404_NOT_FOUND,
    ):
        super().__init__(message, status_code)


class CredentialsException(AppError):
    def __init__(
        self,
        message="Credenciais inválidas",
        status_code=status.HTTP_400_BAD_REQUEST,
    ):
        super().__init__(message, status_code)


class UserWithPhoneNumberAlreadyExists(AppError):
    def __init__(
        self,
        message="Usuário com esse número de telefone já registrado",
        status_code=status.HTTP_400_BAD_REQUEST,
    ):
        super().__init__(message, status_code)


class PasswordsDoesNotMatchException(AppError):
    def __init__(
        self,
        message="Senhas não conhecidem",
        status_code=status.HTTP_400_BAD_REQUEST,
    ):
        super().__init__(message, status_code)
