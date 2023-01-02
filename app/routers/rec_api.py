from fastapi import APIRouter
from core.rec import rec

router = APIRouter()

@router.post('/api/rec')
async def rec_program(info: dict):
    return rec(info)
