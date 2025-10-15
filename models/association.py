from sqlalchemy import ForeignKey, Table, Column
from models.basemodel import Base


# Association tables for many-to-many
student_course_link = Table(
    "student_course_link",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True)
)


employee_course_link = Table(
    "employee_course_link",
    Base.metadata,
    Column("employee_id", ForeignKey("employees.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True)
)