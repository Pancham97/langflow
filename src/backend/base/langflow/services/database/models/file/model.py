from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel, Column, String

from langflow.schema.serialize import UUIDstr


class File(SQLModel, table=True):  # type: ignore[call-arg]
    id: UUIDstr = Field(default_factory=uuid4, primary_key=True)
    # user_id: UUID = Field(foreign_key="user.id")
    user_id: UUID = Field(sa_column=Column(String(36)))
    name: str = Field(unique=True, nullable=False)
    path: str = Field(nullable=False)
    size: int = Field(nullable=False)
    provider: str | None = Field(default=None)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
