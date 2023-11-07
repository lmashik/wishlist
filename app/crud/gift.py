from app.core.db import AsyncSessionLocal
from app.models.gift import Gift
from app.schemas.gift import GiftCreate


async def create_gift(
        new_gift: GiftCreate
) -> Gift:
    new_gift_data = new_gift.model_dump()
    db_gift = Gift(**new_gift_data)

    async with AsyncSessionLocal() as session:
        session.add(db_gift)
        await session.commit()
        await session.refresh(db_gift)
    return db_gift