from fastapi import APIRouter

from api.routes.gift import router as gift_router

main_router = APIRouter()

main_router.include_router(
    gift_router,
    prefix='/gifts',
    tags=['Gifts'],
)
