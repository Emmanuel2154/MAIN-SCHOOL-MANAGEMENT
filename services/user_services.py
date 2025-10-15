from storage import db
from models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user_schema import CreateUserSchema

async def create_user(session: AsyncSession, user_data: CreateUserSchema):
    data = user_data.model_dump()
    user = User(**data)
    await db.save(session, user)
    print(user)
    return user
