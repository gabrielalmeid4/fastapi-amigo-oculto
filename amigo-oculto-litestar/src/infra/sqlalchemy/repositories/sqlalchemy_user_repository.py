from typing import Coroutine
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.entities.user_entity import User
from domain.repositories.user_repository import UserRepository
from infra.sqlalchemy.models.user_model import UserModel


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__()

    async def get_user_by_id(self, user_id: UUID) -> Coroutine[None, None, User]:
        query = select(UserModel).where(UserModel.id == user_id)
        user_found = await self.session.scalar(query)
        if user_found:
            return User(user_found.phone_number, user_found.name, user_found.password)
        return None

    async def get_user_by_phone_number(
        self, phone_number: str
    ) -> Coroutine[None, None, User]:
        query = select(UserModel).where(UserModel.phone_number == phone_number)
        user_found = await self.session.scalar(query)
        if user_found:
            return User(user_found.phone_number, user_found.name, user_found.password)
        return None

    async def create(self, to_be_created: User) -> User:
        user_model = UserModel(**to_be_created.__dict__)
        self.session.add(user_model)
        await self.session.commit()
        await self.session.refresh(user_model)
        return User(user_model.phone_number, user_model.name, user_model.password)
