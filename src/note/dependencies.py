from fastapi import Depends

from src.database import db
from src.note.model import NotesOrm
from src.note.repository import PostgresqlNoteRepository, NoteRepository
from src.note.services import NoteService


def get_note_model():
    return NotesOrm


def get_note_repository(
    model=Depends(get_note_model),
) -> NoteRepository:
    return PostgresqlNoteRepository(model)


def get_note_services(
    repository=Depends(get_note_repository),
) -> NoteService:
    return NoteService(repository)
