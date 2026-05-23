"""Settings routes — /api/settings"""

from fastapi import APIRouter
from models.schemas import AppSettings
from services.db_service import get_settings, save_setting

router = APIRouter()


@router.get("/")
async def get_all():
    return get_settings()


@router.put("/")
async def update_settings(body: AppSettings):
    for key, val in body.model_dump().items():
        save_setting(key, val)
    return get_settings()


@router.put("/{key}")
async def update_one(key: str, value: dict):
    save_setting(key, value.get("value"))
    return {"key": key, "updated": True}
