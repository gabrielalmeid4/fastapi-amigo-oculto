import enum
from datetime import datetime
from uuid import UUID

from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from infra.sqlalchemy.models.base import Base
from infra.sqlalchemy.models.constants import Status


class EventModel(Base):
    __tablename__ = "events"

    uuid: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[enum.Enum] = mapped_column(enum.Enum(Status), nullable=False)
    started_at: Mapped[datetime] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)
