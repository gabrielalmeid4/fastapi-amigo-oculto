class AppError(Exception):
    def __init__(self, message="Erro desconhecido", status_code=500):
        self.detail = message
        self.status_code = status_code
        super().__init__(message)

    @property
    def code(self):
        return __class__.__name__
