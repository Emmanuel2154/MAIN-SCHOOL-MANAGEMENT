from models.basemodel import BaseModel, Base
from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import Mapped, mapped_column


class Student(Base, BaseModel):
    __tablename__ = "students"
    
    student_first_name: Mapped[str] = mapped_column()
    student_middle_name: Mapped[str] = mapped_column()
    student_last_name: Mapped[str] = mapped_column()
    student_gender: Mapped[str] = mapped_column()
    student_address: Mapped[str] = mapped_column()
    student_email: Mapped[str] = mapped_column()
    student_username: Mapped[str] = mapped_column()
    student_phone_number: Mapped[str] = mapped_column()
    student_password: Mapped[str] = mapped_column()
    student_role: Mapped[str] = mapped_column()
    student_date_of_birth: Mapped[int] = mapped_column()

    # student_age: Mapped[int] = mapped_column()