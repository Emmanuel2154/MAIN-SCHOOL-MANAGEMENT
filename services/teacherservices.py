from models.teacher import Teacher

def create_new_teacher(teacher_dict: dict) -> dict:
    """create new teacher"""
    teacher = Teacher(**teacher_dict)
    return teacher
