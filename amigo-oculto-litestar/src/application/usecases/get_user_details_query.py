from dataclasses import dataclass

from domain.repositories.user_repository import UserRepository


@dataclass
class GetUserDetailsQuery:
    def __init__(
        self,
        user_repository: UserRepository,
    ):
        self.user_repository = user_repository

    async def search(self, user_phone_number: str):
        user = await self.user_repository.get_user_by_phone_number(user_phone_number)
        return user
