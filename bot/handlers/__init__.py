from aiogram import Router

from .start import router as common_router
from .photo import router as photo_router


def get_routers() -> list[Router]:
    return [common_router, photo_router]
