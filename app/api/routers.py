from fastapi import APIRouter

from app.api.endpoints import (
    gift_router,
    index_router,
)

main_router = APIRouter()

main_router.include_router(
    gift_router,
    prefix='/gifts',
    tags=['Gifts'],
)
main_router.include_router(
    index_router,
    tags=['Index Page'],
)
