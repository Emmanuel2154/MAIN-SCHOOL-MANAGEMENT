from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///mysqlalchemy.db", echo=True)

class Student(Base):
    __tablename__ = "students"
    id = Column(String, primary_key=True)
    student_name = Column(String)
    student_gender = Column(String)
    student_address = Column(String)
    student_role = Column(String)
    student_age = Column(Integer, nullable=True)

class Employee(Base):
    __tablename__ = "employees"
    id = Column(String, primary_key=True)
    employee_name = Column(String)
    employee_gender = Column(String)
    employee_contact_information = Column(Integer)
    employee_address = Column(String)
    employee_role = Column(String)
    
Base.metadata.create_all(engine)

def add_student_to_database(student_dict: dict):
    with Session(engine) as session:        
        student_obj = Student(**student_dict)
        session.add(student_obj)
        # print(student_obj)
        session.commit()
        print("Student has been saved to database!!")

def add_employee_to_database(employee_dict: dict):
    with Session(engine) as session:
        employee_obj = Employee(**employee_dict)
        session.add(employee_obj)
        session.commit()
        print("Employee has been saved to database!!")