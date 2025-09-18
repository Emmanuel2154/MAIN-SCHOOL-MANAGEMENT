from storage import db


async def yield_session():
    async for session in db.get_session():
        yield session