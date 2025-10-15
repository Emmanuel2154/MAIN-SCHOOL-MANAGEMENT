from models.course import Course
from models.student import Student
from models.employee import Employee
from schemas.course_schema import CreateCourseSchema
from storage import db
from sqlalchemy.ext.asyncio import AsyncSession

async def create_course(session: AsyncSession, course_data: CreateCourseSchema):
    new_data = course_data.model_dump()
    course = Course(**new_data)
    await db.save(session, course)
    return{
        "status": "success",
        "data": course
    }

async def assign_student_to_course(session: AsyncSession, course_id, student_id, ):
    try:
        student = await db.get_by_id(session, Student, student_id)
        course = await db.lazy_load(session, Course, "students", course_id)
        if not student or not course:
            return{
                "status": "Failed",
                "error_message": "Make sure student_id and course_id is correct..."
            }
        course.students.append(student)
        await db.save(session, course)
    except Exception as e:
        raise ValueError(e)
    return{
        "status": "success",
        "data": f"{student.student_first_name} added to {course.course_name}"
    } 

async def assign_employee_to_course(session: AsyncSession, course_id, employee_id):
    employee = await db.get_by_id(session, Employee, employee_id)
    course = await db.get_by_id(session, Course, course_id)
    if not employee or not course:
        return{
            "status": "Failed",
            "error_message": "Make sure employee_id and course_id is correct..."
        }
    course.employees.append(employee)
    await db.save(session, course)
    return{
        "status": "success",
        "data": f"{employee.employee_name} added to {course.course_name}"
    }