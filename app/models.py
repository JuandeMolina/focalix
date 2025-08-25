from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Task(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=False)
    description: so.Mapped[Optional[str]] = so.mapped_column(sa.Text)
    type: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    created_at: so.Mapped[sa.DateTime] = so.mapped_column(
        sa.DateTime, server_default=sa.func.now()
    )
    due_date: so.Mapped[Optional[sa.DateTime]] = so.mapped_column(sa.DateTime)
    completed: so.Mapped[bool] = so.mapped_column(sa.Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.title}>"
