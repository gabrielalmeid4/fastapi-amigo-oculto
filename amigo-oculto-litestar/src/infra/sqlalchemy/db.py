from typing import AsyncGenerator

from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.settings import settings
from infra.sqlalchemy.models.base import Base

engine: Engine = create_async_engine(settings.DATABASE_URL)


async def create_tables():
    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)


async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        try:
            yield session
        except Exception as err:
            await session.rollback()
            raise err
        finally:
            await session.close()
