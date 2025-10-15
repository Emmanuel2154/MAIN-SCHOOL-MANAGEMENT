from models.basemodel import BaseModel, Base
from models.association import student_course_link, employee_course_link
from sqlalchemy.orm import relationship, Mapped, mapped_column


class Course(BaseModel, Base):
    __tablename__ = "courses"

    course_name: Mapped[str] = mapped_column(unique=True, nullable=False)
    course_code: Mapped[str] = mapped_column(unique=True, nullable=False)
    course_description: Mapped[str] = mapped_column(nullable=True)

    # Relationships
    students = relationship("Student", secondary=student_course_link, back_populates="courses")
    employees = relationship("Employee", secondary=employee_course_link, back_populates="courses", lazy="selectin")
