from  models.student import Student
from schemas.student_schema import CreateStudentSchema
from db_sql import student_to_db
from sql_alchemy import add_student_to_database

def create_new_student(student_dict: dict) -> Student:
    """Create Student"""
    data = CreateStudentSchema(**student_dict)
    data_dict = data.model_dump()
    
    student = Student(**data_dict)
    """call the method that saves it to the file"""
    student.save_to_json()
    return student

def add_student_to_db(student_dict: dict) -> Student:
    """Create Student"""
    print("Enter student_name")
    student_name = input(">")
    print("Enter student_gender")
    student_gender = input(">")
    print("Enter student_address")
    student_address = input(">")
    print("Enter student_role: [headboy, headgirl, assistant headboy, assitant headboy]")
    student_role = input(">")
    print("Enter student_age")
    student_age = input(">")

    student_dict.update({
        "student_name": student_name,
        "student_gender": student_gender,
        "student_address": student_address,
        "student_role": student_role,
        "student_age": student_age
    })
    data = CreateStudentSchema(**student_dict)
    data_dict = data.model_dump()
    
    student = Student(**data_dict)
    """call function to save to database"""
    add_student_to_database(student.to_dict())
    return student


