from  models.student import Student
from schemas.student_schema import CreateStudentSchema
from storage.database import DBstorage
from sqlalchemy.ext.asyncio import AsyncSession
from storage import db

async def create_new_student(session: AsyncSession, student_dict: CreateStudentSchema):
    data = student_dict.model_dump()
    student = Student(**data)
    await db.save(session, student)
    await session.refresh(student)
    return {
        "status": "success",
        "data": student.to_dict()
    }

async def fetch_students(session: AsyncSession):
    all_student = await db.get_by_class(session, Student)
    return [student.to_dict() for student in all_student]

async def get_student_by_id(session: AsyncSession, student_id):
    student = await db.get_by_id(session, Student, student_id)
    if student is None:
        print("Student is not available in th DB")
        return {}
    return {
        "status": "success",
        "data": student
    }

async def get_student_by_user_id(session: AsyncSession, user_id):
    student = await db.get_by_user_id(session, Student, user_id)
    if student is None:
        print("User is not available in DB")
        return{}
    await session.refresh(student, ["user"])
    return {
        "status": "success",
        "data": student
    }

async def search_student_by_column_name(session: AsyncSession, column_name):
    column = await db.get_by_column_name(session, Student, column_name)
    return {
        "status": "success",
        "data": column
    }

async def update_student(session: AsyncSession, student_id, key, value):
    new_info = await db.update_info(session, Student, student_id, key, value)
    return {
        "status": "success",
        "data": new_info
    }

async def delete_student(session: AsyncSession, student_id):
    deleted_info = await db.delete_by_id(session, Student, student_id)
    return {
        "status": "success",
        "data": deleted_info
    }

