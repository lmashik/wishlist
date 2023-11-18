from fastapi import APIRouter

from api.crud.gift import create_gift
from api.schemas.gift import GiftCreate, GiftDB

router = APIRouter()


@router.post(
    '/',
    response_model=GiftDB,
    response_model_exclude_none=True,
)
async def create_new_gift(
        gift: GiftCreate,
):
    new_gift = await create_gift(gift)
    return new_gift
