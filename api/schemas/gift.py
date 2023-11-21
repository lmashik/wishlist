from typing import Any, Optional

from pydantic import BaseModel, Extra, Field, field_validator

from api.constants import NAME_MAX_LENGTH, NAME_MIN_LENGTH


class GiftBase(BaseModel):
    """Базовая схема подарка."""
    name: Optional[str] = Field(
        None,
        title='Name',
        min_length=NAME_MIN_LENGTH,
        max_length=NAME_MAX_LENGTH,
    )
    comment: Optional[str] = Field(None, title='Comment')
    link: Optional[str] = Field(None, title='Link')
    price: Optional[int] = Field(None, title='Price')

    class Config:
        title = 'Base gift schema'


class GiftCreate(GiftBase):
    """Схема подарка для создания."""
    name: str = Field(
        ...,
        title='Name',
        min_length=NAME_MIN_LENGTH,
        max_length=NAME_MAX_LENGTH,
    )

    @field_validator('name')
    def name_cannot_be_null(cls, value: str):
        if not value:
            raise ValueError('The name cant be empty!')
        return value

    class Config:
        title = 'Create gift schema'
        extra = Extra.forbid


class GiftDB(GiftCreate):
    """Схема подарка для получения."""
    id: Any = Field(..., title='uuid')

    class Config:
        title = 'DB gift schema'
        from_attributes = True
        schema_extra = {
            'example': {
                'id': 'ed0c3161-7b93-49fd-80fb-fb23de937565',
                'name': 'Джемпер Zarina',
                'comment': 'Или похожую по цвету',
                'link':
                    'https://www.ozon.ru/product/dzhemper-zarina-1175589199/',
                'price': 1313
            }
        }
