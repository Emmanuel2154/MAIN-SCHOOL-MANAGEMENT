from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from services.auth import register_user, login_user, verify_user
from pydantic import EmailStr
from storage import db
from schemas.user_schema import CreateUserSchema

auth_router = APIRouter()

@auth_router.post("/register")
async def register(user_data: CreateUserSchema, session: AsyncSession = Depends(db.get_session)):
    response = await register_user(session, user_data)
    return response

@auth_router.post('/login')
async def login(email: EmailStr, password: str, session: AsyncSession = Depends(db.get_session)):
    user = await login_user(session, email, password)
    return user

@auth_router.post('/verify')
async def verify(token : int, session: AsyncSession = Depends(db.get_session)):
    user = await verify_user(session, token)
    return user 