from fastapi import APIRouter


router = APIRouter()


@router.get('')
def get_all_notes():
    ...


@router.post('')
def add_note():
    ...