from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from infra.sqlalchemy.models.base import Base


class ParticipationModel(Base):
    __tablename__ = "participations"

    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    event_id: Mapped[str] = mapped_column(ForeignKey("events.uuid"), nullable=False)
    hidden_friend_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )
