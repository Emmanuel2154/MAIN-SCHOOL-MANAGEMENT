from fastapi import FastAPI, Depends,  APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from storage import db
from services.employee_services import create_new_employee, fetch_employees, get_employee_by_id, update_employee, delete_employee, search_employee_by_column_name
from schemas.employee_schema import CreateEmployeeSchema

employee_router = APIRouter(prefix="/api/v1/employees", tags=["Employees"])

@employee_router.post("/employee")
async def add_employee(
    employee_data: CreateEmployeeSchema, session: AsyncSession = Depends(db.get_session)
):
    new_employee = await create_new_employee(session, employee_data)
    return new_employee

@employee_router.post("/employee/update/{employee_id}/{key}/{value}")
async def update_employee_info(employee_id: str, key: str, value, session: AsyncSession = Depends(db.get_session)):
    new_info = await update_employee(session, employee_id, key, value)
    return new_info

@employee_router.delete("/employee/delete/{employee_id}")
async def delete_admin_info(employee_id: str, session: AsyncSession = Depends(db.get_session)):
    deleted_employee = await delete_employee(session, employee_id)
    return deleted_employee

@employee_router.get("/employee")
async def get_all_employee(session: AsyncSession = Depends(db.get_session)):
    all_employees = await fetch_employees(session)
    return all_employees

@employee_router.get("/employee/{employee_id}")
async def get_employee(employee_id: str, session: AsyncSession = Depends(db.get_session)):
    employee = await get_employee_by_id(session, employee_id)
    return employee

@employee_router.get("/employee/column_name/{column_name}")
async def search_column_name(column_name, session: AsyncSession = Depends(db.get_session)):
    employee = await search_employee_by_column_name(session, column_name)
    return employee