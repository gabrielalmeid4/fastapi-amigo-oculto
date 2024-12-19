from pydantic import BaseModel


class AuthResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
