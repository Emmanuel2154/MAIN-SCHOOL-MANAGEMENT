from models.basemodel import BaseModel, Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import Optional
from models.association import employee_course_link

class Employee(BaseModel, Base):
    __tablename__ = "employees"
    
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    employee_name: Mapped[str] = mapped_column()
    employee_gender: Mapped[str] = mapped_column()
    employee_contact_information: Mapped[str] = mapped_column()
    employee_address: Mapped[str] = mapped_column()
    employee_role: Mapped[str] = mapped_column()

    user = relationship("User", back_populates="employee")
    courses = relationship("Course", secondary=employee_course_link, back_populates="employees")
    