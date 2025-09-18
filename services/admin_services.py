from models.admin import Admin
from schemas.admin_schema import CreateAdminSchema
from storage.database import DBstorage
from sqlalchemy.ext.asyncio import AsyncSession

db = DBstorage()

async def create_new_admin(session: AsyncSession, admin_dict: CreateAdminSchema):
    new_data = admin_dict.model_dump()
    admin = Admin(**new_data)
    await db.save(session, admin)
    await session.refresh(admin)
    return {
        "status": "success",
        "data": admin.to_dict()
    }

async def get_admin_by_id(session: AsyncSession, admin_id: str):
    admin = await db.get_by_id(session, Admin, admin_id)
    print(admin)
    if admin is None:
        print("Admin is not available in th DB")
        return {}
    # await session.refresh(admin)
    return admin.to_dict()

async def fetch_admins(session: AsyncSession):
    all_admin = await db.get_by_class(session, Admin)
    return [admin.to_dict() for admin in all_admin]

async def search_admin_by_column_name(session: AsyncSession, column_name):
    column = await db.get_by_column_name(session, Admin, column_name)
    return column

async def update_admin(session: AsyncSession, admin_id, key, value):
    new_info = await db.update_info(session, Admin, admin_id, key, value)
    return new_info
    
async def delete_admin(session: AsyncSession, admin_id):
    deleted_info = await db.delete_by_id(session, Admin, admin_id)
    return deleted_info

