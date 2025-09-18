from services.student_services import create_new_student, get_student_by_id
from myalchemy import add_student_to_database
from services.employee_services import add_employee_to_db
from services.admin_services import create_new_admin
from storage.database import DBstorage
from models.student import Student
from models.employee import Employee
from models.admin import Admin
import asyncio
from utils.getSession import yield_session


from uuid import uuid4

from data import student as student_dict, employee as employee_dict, admin as admin_dict

from data import employee as employee_dict



db = DBstorage()

async def main(): 
       
    try:
    
        # add_student_to_database(student_dict)
        # db = DBstorage()
       
            # new_user = User(id=str(uuid4()), email="anything", password="anything")
        #     db.add(session, new_user)
        #     await session.commit()
        await db.drop_tables()
        
        await db.create_table()
        # async for session in db.get_session():
        #     result = await create_new_student(session, student_dict)
        #     print(result)
        # # async for session in db.get_session():
        #     result = await get_student_by_id(session, Student, "S: de71a62e-b5cb-4fc3-81c3-854d659750c7")
        #     print(result)
        
        # async for session in db.get_session():
        #     await update_student_info(session, Admin, "A: 51d4358b-eb8f-41d9-a327-2ea7fb430ade", "admin_name", "Olamide")
        
        # async for session in db.get_session():
        #     await delete_admin_info(session, Admin, "A: 430127d3-2f2d-4581-a7b9-f5e9c8731683")

        # async for session in db.get_session():
        # result = await get_all_admin(Admin, "male")
        # print(result)
        
    except ValueError as e:
        print(e)
        
asyncio.run(main())