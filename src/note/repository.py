from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.note.model import NotesOrm


class NoteRepository(ABC):
    @abstractmethod
    async def get_by_id_or_none(
        self, session: AsyncSession, user_id: int
    ) -> Sequence[NotesOrm | None]: ...

    @abstractmethod
    async def get_by_title_or_none(
        self, session: AsyncSession, title: str
    ) -> NotesOrm | None: ...

    @abstractmethod
    async def create_note(
        self, session: AsyncSession, user_id: int, title: str, description: str
    ) -> NotesOrm: ...


@dataclass
class PostgresqlNoteRepository(NoteRepository):
    model: NotesOrm = field(default=NotesOrm)

    async def get_by_id_or_none(
        self, session: AsyncSession, user_id: int
    ) -> Sequence[NotesOrm | None]:
        query = select(self.model).where(self.model.user_id == user_id)
        response = await session.scalars(query)
        return response.all()

    async def get_by_title_or_none(
        self, session: AsyncSession, title: str
    ) -> NotesOrm | None:
        query = select(self.model).where(self.model.title == title)
        response = await session.scalars(query)
        return response.one()

    async def create_note(
        self, session: AsyncSession, user_id: int, title: str, description: str
    ) -> NotesOrm:
        note = self.model(user_id=user_id, title=title, description=description)
        session.add(note)
        await session.flush()
        await session.commit()
        return note

    async def get_all(self, session: AsyncSession) -> Sequence[NotesOrm | None]:
        query = select(self.model)
        response = await session.scalars(query)
        return response.all()
