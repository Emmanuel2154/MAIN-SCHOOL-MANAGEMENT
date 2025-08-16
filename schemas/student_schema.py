from pydantic import BaseModel, model_validator
from typing import Literal

class CreateStudentSchema(BaseModel):
    """Student's pydantic attributes"""
    student_name: str
    student_gender: Literal['male', 'female']
    student_address: str
    student_role: Literal['headboy', 'headgirl', 'assistant headboy', 'assitant headboy', 'normal student']
    student_age: int

    @model_validator(mode="before")
    def normalize_case(cls, dictionary):
        for field in ["student_gender", "student_role"]:
            if field in dictionary and isinstance (dictionary[field], str):
                dictionary[field] = dictionary[field].lower()
        return dictionary