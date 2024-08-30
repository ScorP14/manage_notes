from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.database import db, BaseDataBase

from src.note.model import NotesOrm  # ?!

from src.note.router import router as note_router
from src.auth.router import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Start App")
    async with db.engine.begin() as connect:
        await connect.run_sync(BaseDataBase.metadata.create_all)
    yield
    print("Stop App")
    await db.dispose()


def get_app() -> FastAPI:

    application = FastAPI(
        lifespan=lifespan,
        title="Заметки",
        description="API Для управления заметками",
    )
    application.include_router(note_router, prefix="/note")
    application.include_router(auth_router, prefix="/auth")

    return application
