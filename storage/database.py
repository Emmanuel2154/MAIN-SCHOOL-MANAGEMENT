from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from models.basemodel import Base
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import selectinload
from sqlalchemy.future import select
from pydantic import EmailStr
from models import student, employee, admin, user
class DBstorage:
    def __init__(self, db_url: str = "sqlite+aiosqlite:///mysqlalchemy.db"):
        self.__engine = create_async_engine(db_url, echo=False)
        self.__session_maker = async_sessionmaker(self.__engine, expire_on_commit=False)

    async def create_table(self):
        """Creating a table in the database"""
        async with self.__engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    
    async def drop_tables(self):
        async with self.__engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    async def get_session(self):
        async with self.__session_maker() as session:
            yield session
    
    def add(self, session: AsyncSession, obj):
        session.add(obj)
    
    async def save(self, session: AsyncSession, obj = None):
        if obj:
            self.add(session, obj)
        await session.commit()
    
    async def get_by_class(self, session: AsyncSession, cls: Base):
        smtp = select(cls)
        result = await session.execute(smtp)
        return result.scalars().all()
    
    async def get_by_id(self, session: AsyncSession, cls: Base, object_id:str):
        result = await session.execute(select(cls).where(cls.id == object_id))
        return result.scalar_one_or_none()
    

    async def get_by_column_name(self, session: AsyncSession, cls: Base, column_name: str):
        column = getattr(cls, column_name,  None)
        if column is None:
            return (f"{column_name} not found in db")
        smtp = await session.execute(select(column))
        result = [row[0] for row in smtp.all()]
        return result
    
    async def update_info(self, session: AsyncSession, cls: Base, id: str, key: str, value):
        result = await self.get_by_id(session, cls, id)
        if not result:
            return ("Record not found in db")
        setattr(result, key, value)
        await session.commit()
        return result
    
    async def get_by_user_id(self, session: AsyncSession, cls: Base, user_id: str):
        result = await session.execute(select(cls).where(cls.user_id == user_id))
        return result.scalars().first()
    
    async def delete_by_id(self, session: AsyncSession, cls: Base, id: str):
        result = await self.get_by_id(session, cls, id)
        if not  result:
            return (f"{cls.__name__} with {id} not in DB")
        await session.delete(result)
        await session.commit()
        return result
    
    async def lazy_load(self, session, model, relationship, object_id):
        result = await session.execute(select(model).options(selectinload(getattr(model, relationship))).where(model.id == object_id))
        return result.scalar_one_or_none()
    
    async def get_by_email(self, session, model, email: EmailStr):
        result = await session.execute(select(model).where(model.email == email))
        return result.scalar_one_or_none()
    
    async def verify(self, session: AsyncSession, cls: Base, token):
        result = await session.execute(select(cls).where(cls.reset_token == token))
        return result

