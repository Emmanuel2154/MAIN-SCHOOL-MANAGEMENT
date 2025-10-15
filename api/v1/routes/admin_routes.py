from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from services.admin_services import create_new_admin, get_admin_by_id, fetch_admins, update_admin, delete_admin, search_admin_by_column_name
from schemas.admin_schema import CreateAdminSchema
from storage import db 

admin_router = APIRouter()

@admin_router.post("/admin")
async def add_admin(
    admin_data: CreateAdminSchema, session: AsyncSession = Depends(db.get_session)
):
    new_admin = await create_new_admin(session, admin_data)
    return new_admin

@admin_router.post("/admin/update/{admin_id}/{key}/{value}")
async def update_admin(admin_id: str, key: str, value, session: AsyncSession = Depends(db.get_session)):
    new_info = await update_admin(session, admin_id, key, value)
    return new_info

@admin_router.delete("/admin/delete/{admin_id}")
async def delete_admin_info(admin_id: str, session: AsyncSession = Depends(db.get_session)):
    deleted_admin = await delete_admin(session, admin_id)
    return deleted_admin

@admin_router.get("/admin")
async def get_all_admin(session: AsyncSession = Depends(db.get_session)):
    all_admins = await fetch_admins(session)
    return all_admins

@admin_router.get("/admin/{admin_id}")
async def get_admin(admin_id: str, session: AsyncSession = Depends(db.get_session)):
    admin = await get_admin_by_id(session, admin_id)
    return admin

@admin_router.get("/admin/column_name/{column_name}")
async def search_column_name(column_name, session: AsyncSession = Depends(db.get_session)):
    admin = await search_admin_by_column_name(session, column_name)
    return admin