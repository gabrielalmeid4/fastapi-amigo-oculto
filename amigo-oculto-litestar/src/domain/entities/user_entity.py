from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID


@dataclass
class User:
    id: UUID = field(init=False)
    phone_number: str
    name: str
    password: str
    joined_at: datetime = field(init=False)
    edited_at: datetime = field(init=False)
