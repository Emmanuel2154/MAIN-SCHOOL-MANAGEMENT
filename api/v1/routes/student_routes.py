from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from services.student_services import create_new_student, fetch_students, get_student_by_id, search_student_by_column_name, update_student, delete_student, get_student_by_user_id
from schemas.student_schema import CreateStudentSchema
from storage import db 

student_router = APIRouter(prefix="/api/v1/students", tags=["Students"])

@student_router.post("/")
async def add_student(
    student_data: CreateStudentSchema,
    session: AsyncSession = Depends(db.get_session)
):
    response = await create_new_student(session, student_data)
    return response

@student_router.post("/{student_id}/{key}/{value}")
async def update_admin(student_id: str, key: str, value, session: AsyncSession = Depends(db.get_session)):
    new_info = await update_student(session, student_id, key, value)
    return new_info

@student_router.delete("/{student_id}")
async def delete_student_info(student_id: str, session: AsyncSession = Depends(db.get_session)):
    deleted_student = await delete_student(session, student_id)
    return deleted_student

@student_router.get("/")
async def get_all_student(session: AsyncSession = Depends(db.get_session)):
    all_students = await fetch_students(session)
    return all_students

@student_router.get("/{student_id}")
async def get_student(student_id: str, session: AsyncSession = Depends(db.get_session)):
    student = await get_student_by_id(session, student_id)
    return student

@student_router.get("/by_user/{user_id}")
async def get_user_by_user(user_id: str, session: AsyncSession = Depends(db.get_session)):
    user = await get_student_by_user_id(session, user_id)
    return user

@student_router.get("/search/{column_name}")
async def search_column_name(column_name, session: AsyncSession = Depends(db.get_session)):
    student = await search_student_by_column_name(session, column_name)
    return student