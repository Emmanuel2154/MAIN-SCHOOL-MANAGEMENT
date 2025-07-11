from models.student import Student


def create_new_student(student_dict: dict) -> dict:
    """Create Student"""
    student = Student(**student_dict)
    return student
