from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from typing import Sequence, Annotated

from src.auth.router import get_current_user

from src.database import db
from src.note.dependencies import get_note_services
from src.note.schemas import NoteRead, NoteCreate
from src.note.services import NoteService
from src.user.schemas import UserRead


router = APIRouter(tags=["note"])


@router.get(
    path="",
    response_model=Sequence[NoteRead],
    status_code=status.HTTP_200_OK,
    description="Авторизованный пользователь может получить список своих заметок",
)
async def get_note_by_user(
    current_user: Annotated[UserRead, Depends(get_current_user)],
    services: Annotated[NoteService, Depends(get_note_services)],
    session: Annotated[AsyncSession, Depends(db.get_session)],
):
    data = await services.get_note_by_user_id(session, current_user.id)
    return data


@router.post(
    path="",
    response_model=NoteRead,
    status_code=status.HTTP_201_CREATED,
    description="Авторизованный пользователь может создать для себя заметку",
)
async def create_note(
    data: Annotated[NoteCreate, Depends()],
    current_user: Annotated[UserRead, Depends(get_current_user)],
    services: Annotated[NoteService, Depends(get_note_services)],
    session: Annotated[AsyncSession, Depends(db.get_session)],
):
    data = await services.create_note(session, current_user.id, data)
    return data
