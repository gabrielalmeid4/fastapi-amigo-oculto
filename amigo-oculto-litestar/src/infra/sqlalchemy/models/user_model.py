from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from infra.sqlalchemy.models.base import Base


class UserModel(Base):
    __tablename__ = "users"

    phone_number: Mapped[str] = mapped_column(unique=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid4()
    )
    joined_at: Mapped[datetime] = mapped_column(default=datetime.now(), nullable=False)
    edited_at: Mapped[datetime] = mapped_column(
        default=datetime.now(), onupdate=datetime.now(), nullable=False
    )
