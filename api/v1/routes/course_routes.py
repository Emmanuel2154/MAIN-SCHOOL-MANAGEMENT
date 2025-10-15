from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from services.course_services import create_course, assign_student_to_course, assign_employee_to_course
from schemas.course_schema import CreateCourseSchema
from storage import db

course_router = APIRouter(prefix="/api/v1/courses", tags=["Courses"])

@course_router.post("/")
async def add_course(course_data: CreateCourseSchema, session: AsyncSession = Depends(db.get_session)):
    response = await create_course(session, course_data)
    return response

@course_router.post("/{course_id}/add_student/{student_id}")
async def add_student_to_course(student_id, course_id, session: AsyncSession = Depends(db.get_session)):
    response = await assign_student_to_course(session, course_id, student_id)
    return response

@course_router.post("/{course_id}/add_employee/{employee_id}")
async def add_employee_to_course(course_id, employee_id, session: AsyncSession = Depends(db.get_session)):
    response = await assign_employee_to_course(session, course_id, employee_id)
    return response

