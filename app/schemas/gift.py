from typing import Optional

from pydantic import BaseModel, Field

from app.constants import NAME_MAX_LENGTH, NAME_MIN_LENGTH


class GiftCreate(BaseModel):
    name: str = Field(
        ...,
        title='Название',
        min_length=NAME_MIN_LENGTH,
        max_length=NAME_MAX_LENGTH,
    )
    comment: Optional[str]
