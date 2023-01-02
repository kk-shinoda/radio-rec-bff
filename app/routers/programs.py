from fastapi import APIRouter

router = APIRouter()

@router.get('/programs')
async def get_programs():
    return {'message': 'wip'}
