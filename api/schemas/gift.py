from typing import Optional

from pydantic import BaseModel, Field

from api.constants import NAME_MAX_LENGTH, NAME_MIN_LENGTH


class GiftBase(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=NAME_MIN_LENGTH,
        max_length=NAME_MAX_LENGTH,
    )
    comment: Optional[str]
    link: Optional[str]
    price: Optional[int]


class GiftCreate(GiftBase):
    name: str = Field(
        ...,
        min_length=NAME_MIN_LENGTH,
        max_length=NAME_MAX_LENGTH,
    )


class GiftDB(GiftCreate):
    id: str

    class Config:
        from_attributes = True
