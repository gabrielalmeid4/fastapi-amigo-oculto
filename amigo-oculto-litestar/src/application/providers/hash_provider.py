from abc import ABC, abstractmethod


class HashProvider(ABC):
    @abstractmethod
    def hash(self, payload: str) -> str:
        pass

    @abstractmethod
    def verify(self, hash: str, payload: str) -> bool:
        pass
