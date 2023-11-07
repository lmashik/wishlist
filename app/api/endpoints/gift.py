from fastapi import APIRouter

from app.crud.gift import create_gift
from app.schemas.gift import GiftCreate

router = APIRouter()


@router.post('/')
async def create_new_gift(
        gift: GiftCreate,
):
    new_gift = await create_gift(gift)
    return new_gift
