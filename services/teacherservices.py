from models.teacher import Teacher
from schemas.teacher import CreateTeacherSchema
from db_sql import teacher_to_db

def create_new_teacher(student_dict: dict) -> Teacher:
    """Create Student"""
    data = CreateTeacherSchema(**student_dict)
    data_dict = data.model_dump()
 
    teacher = Teacher(**data_dict)
    # call the method that saves it to the file
    teacher.save_to_json()
    return teacher

def add_teacher_to_db(teacher_dict: dict) -> Teacher:
    """Create Teacher"""
    data = CreateTeacherSchema(**teacher_dict)
    data_dict = data.model_dump()
    teacher = Teacher(**data_dict)
    teacher_to_db(**teacher.to_dict())