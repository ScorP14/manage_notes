from fastapi import APIRouter


router = APIRouter()


@router.get("")
async def get_all_notes(): ...


@router.post("")
async def add_note(): ...
