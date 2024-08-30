from dataclasses import dataclass
from typing import Sequence
from src.note.repository import PostgresqlNoteRepository
from src.note.schemas import NoteCreate, NoteRead
from src.services.checking_text.yandex_speller import CheckTextYandexSpeller


@dataclass
class NoteService:
    repository: PostgresqlNoteRepository

    async def create_note(self, session, user_id: int, data: NoteCreate) -> NoteRead:
        note = await self.repository.create_note(
            session=session,
            user_id=user_id,
            title=CheckTextYandexSpeller(data.title).execute(),
            description=CheckTextYandexSpeller(data.description).execute(),
        )
        return NoteRead(**note.__dict__)

    async def get_note_by_user_id(self, session, user_id: int) -> Sequence[NoteRead]:
        data = await self.repository.get_by_id_or_none(session, user_id)
        return [NoteRead(**item.__dict__) for item in data]
