from datetime import datetime, timezone
from sqlalchemy import Integer, String, Boolean, Datetime
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Todo(Base):
    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        index = True
    )

    title: Mapped[str] = mapped_column(
        String,
        index = True
    )
    description: Mapped[str | None] = mapped_column(String)
    completed:  Mapped[bool] = mapped_column(Boolean)
    created_at: Mapped[datetime] = mapped_column(Datetime, default=lambda:datetime.now(timezone.utc))