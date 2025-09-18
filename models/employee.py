from models.basemodel import BaseModel, Base
# from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import mapped_column, Mapped
class Employee(BaseModel, Base):
    __tablename__ = "employees"
    employee_name: Mapped[str] = mapped_column()
    employee_gender: Mapped[str] = mapped_column()
    employee_contact_information: Mapped[str] = mapped_column()
    employee_address: Mapped[str] = mapped_column()
    employee_role: Mapped[str] = mapped_column()