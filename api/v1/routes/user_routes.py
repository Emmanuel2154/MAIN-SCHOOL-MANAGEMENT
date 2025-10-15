from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from services.user_services import create_user
from schemas.user_schema import CreateUserSchema
from storage import db

user_router = APIRouter(prefix="/api/v1/users", tags=["Users"])

# @user_router.post("/")
# async def add_user(
#     user_data: CreateUserSchema,
#     session: AsyncSession = Depends(db.get_session)
# ):
#     response = await create_user(session, user_data)
#     return response