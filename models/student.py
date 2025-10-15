from models.basemodel import BaseModel, Base

from sqlalchemy import String, Integer, Column, ForeignKey
from typing import Optional
from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.association import student_course_link

class Student(BaseModel, Base):
    __tablename__ = "students"
    
    user_id: Mapped[Optional[str]] = mapped_column(ForeignKey("users.id"), default=lambda: str(uuid4()))
    student_first_name: Mapped[str] = mapped_column()
    student_middle_name: Mapped[str] = mapped_column()
    student_last_name: Mapped[str] = mapped_column()
    student_gender: Mapped[str] = mapped_column()
    student_address: Mapped[str] = mapped_column()
    student_phone_number: Mapped[str] = mapped_column()
    student_role: Mapped[str] = mapped_column()
    student_date_of_birth: Mapped[int] = mapped_column()

    user = relationship("User", back_populates="student")
    courses = relationship("Course", secondary=student_course_link, back_populates="students", lazy="selectin")
