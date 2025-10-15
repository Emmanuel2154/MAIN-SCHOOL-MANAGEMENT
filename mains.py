
from storage import db
import asyncio

from models import course, student, employee, association

async def main(): 
       
    try:
        await db.drop_tables()
        await db.create_table()

    except ValueError as e:
        print(e)
        
asyncio.run(main())