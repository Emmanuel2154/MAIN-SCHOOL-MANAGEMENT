from pydantic import BaseModel, model_validator
from typing import Literal

class CreateStudentSchema(BaseModel):
    """Student's pydantic attributes"""
    student_first_name: str
    student_middle_name: str
    student_last_name: str
    student_email: str
    student_phone_number: str
    student_username: str
    student_password: str
    student_gender: Literal['male', 'female']
    student_address: str
    student_role: Literal['headboy', 'headgirl', 'assistant headboy', 'assitant headboy', 'normal student']
    student_date_of_birth: str

    @model_validator(mode="before")
    def normalize_case(cls, dictionary):
        for field in ["student_gender", "student_role"]:
            if field in dictionary and isinstance (dictionary[field], str):
                dictionary[field] = dictionary[field].lower()
        return dictionary