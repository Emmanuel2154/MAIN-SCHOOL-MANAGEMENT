from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from models.basemodel import Base
from sqlalchemy import select
from models import student, employee, admin
class DBstorage:
    def __init__(self, db_url: str = "sqlite+aiosqlite:///mysqlalchemy.db"):
        self.__engine = create_async_engine(db_url, echo=False)
        self.__session_maker = async_sessionmaker(self.__engine)

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
        smtp = await session.execute(select(cls).where(cls.id == object_id))
        return smtp.scalar_one_or_none()
    
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
    
    async def delete_by_id(self, session: AsyncSession, cls: Base, id: str):
        result = await self.get_by_id(session, cls, id)
        print(result)
        if not  result:
            return (f"{cls.__name__} with {id} not in DB")
        await session.delete(result)
        await session.commit()
        return result