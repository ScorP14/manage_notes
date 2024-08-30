from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    description: str | None


class NoteCreate(NoteBase): ...


class NoteRead(NoteBase):
    id: int
    user_id: int
