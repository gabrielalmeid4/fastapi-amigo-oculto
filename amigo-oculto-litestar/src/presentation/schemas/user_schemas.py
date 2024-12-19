from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    password: str
    phone_number: str


class UserSignupSchema(BaseModel):
    confirm_password: str
    name: str
    password: str
    phone_number: str


class UserResponseSchema(BaseModel):
    name: str
    phone_number: str
