from models.employee import Employee
from schemas.employee_schema import CreateEmployeeSchema
# from db_sql import teacher_to_db
from myalchemy import add_employee_to_database
from storage.database import DBstorage
from sqlalchemy.ext.asyncio import AsyncSession

db = DBstorage()
async def create_new_employee(session: AsyncSession, employee_dict: CreateEmployeeSchema):
    new_data = employee_dict.model_dump()
    employee = Employee(**new_data)
    # print(student.to_dict())
    await db.save(session, employee)
    await session.refresh(employee)
    return {
        "status": "success",
        "data": employee.to_dict()
    }

async def add_employee_to_db(employee_dict: dict) -> Employee:
    """Create Employee"""
    data = CreateEmployeeSchema(**employee_dict).model_dump()
    employee = Employee(**data)
    async for session in db.get_session():
        await db.save(session, employee)
        return{
            "status": "success",
            "data": employee.to_dict()
        }

async def fetch_employees(session: AsyncSession):
    all_employee = await db.get_by_class(session, Employee)
    return [employee.to_dict() for employee in all_employee]

async def get_employee_by_id(session: AsyncSession, employee_id):
    employee = await db.get_by_id(session, Employee, employee_id)
    if employee is None:
        print("Employee is not in DB")
        return{}
    return employee.to_dict()

async def search_employee_by_column_name(session: AsyncSession, column_name):
    column = await db.get_by_column_name(session, Employee, column_name)
    return column

async def update_employee(session: AsyncSession, employee_id, key, value):
    new_info = await db.update_info(session, Employee, employee_id, key, value)
    return new_info
    

async def delete_employee(session: AsyncSession, employee_id):
    deleted_info = await db.delete_by_id(session, Employee, employee_id)
    return deleted_info
