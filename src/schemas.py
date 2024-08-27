from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


class Note(BaseModel):
    author: User
    title: str
    description: str
