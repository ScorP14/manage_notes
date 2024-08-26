from fastapi import FastAPI

from src.router import router as note_router


def get_app():
    app = FastAPI(description='API Для ')

    app.include_router(note_router, prefix='/note')

    return app
