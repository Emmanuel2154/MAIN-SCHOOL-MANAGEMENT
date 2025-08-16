from  models.student import Student
from schemas.student import CreateStudentSchema
from db_sql import student_to_db

def create_new_student(student_dict: dict) -> Student:
    """Create Student"""
    data = CreateStudentSchema(**student_dict)
    data_dict = data.model_dump()
    # student = Student(**data.model_dump())
    student = Student(**data_dict)
    # call the method that saves it to the file
    student.save_to_json()
    return student



def add_student_to_db(student_dict: dict) -> Student:
    """Create Student"""
    data = CreateStudentSchema(**student_dict)
    data_dict = data.model_dump()
    # student = Student(**data.model_dump())
    student = Student(**data_dict)
    # call function to save to database
    student_to_db(student.to_dict())
    
    return student


