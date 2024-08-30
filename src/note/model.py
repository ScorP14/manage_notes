from src.database import BaseDataBase
from sqlalchemy.orm import Mapped, mapped_column


class NotesOrm(BaseDataBase):
    __tablename__ = "notes"

    user_id: Mapped[int]
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str | None]

    def __repr__(self):
        return f"<{self.__class__.__name__}-id-{self.id}>"

    def __str__(self):
        return f"{self.id}-{self.title}"
