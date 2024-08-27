from fastapi import FastAPI

from src.note.router import router as note_router


def get_app() -> FastAPI:

    app = FastAPI(
        title="Заметки",
        description="API Для управления заметками",
    )
    app.include_router(note_router, prefix="/note")

    return app
