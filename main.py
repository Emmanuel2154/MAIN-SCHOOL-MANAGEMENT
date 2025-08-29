from services.student_services import create_new_student
# from sql_alchemy import add_student_to_database
# from services.employee_services import add_employee_to_db, create_new_employee
from storage.database import DBstorage
from models.student import Student
from models.employee import Employee
from models.user import User
import asyncio

from uuid import uuid4
# from utils.fiile_handler import append_file
from data import student as student_dict
# from data import employee as employee_obj
# from pprint import pprint


db = DBstorage()

async def main(): 
       
    try:
    
        # add_student_to_database(student_dict)

        # db = DBstorage()
        # async for session in db.get_session():
        #     new_user = User(id=str(uuid4()), email="anything", password="anything")
        #     db.add(session, new_user)
        #     await session.commit()
        # await db.drop_tables()
        # await db.create_table()
        # result = await create_new_student(student_dict)
        # print(result)
        async for session in db.get_session():
            
    except ValueError as e:
        print(e)
    
asyncio.run(main())