from dotenv import load_dotenv
import os
import asyncpg
from fastapi import Depends

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

async def get_db():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()