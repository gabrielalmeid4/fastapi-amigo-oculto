from abc import ABC, abstractmethod
from typing import TypedDict


class TokenData(TypedDict):
    sub: str
    exp: int


class TokenProvider(ABC):
    @abstractmethod
    def encode(self, data: dict, expires: int) -> TokenData:
        pass

    @abstractmethod
    def decode(self, token: str) -> str:
        pass
