from fastapi import FastAPI

from api.core.config import settings
from api.routes import main_router

app = FastAPI(title=settings.app_title)
app.include_router(main_router)
